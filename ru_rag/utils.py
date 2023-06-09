from typing import List

from huggingface_hub import snapshot_download
from llama_cpp import Llama

from ru_rag.token import Token


def get_message_tokens(model: Llama, token: int, content: str) -> List[int]:
    message_tokens = model.tokenize(content.encode("utf-8"))
    message_tokens.insert(1, token)
    message_tokens.insert(2, Token.LINEBREAK.value)
    message_tokens.append(model.token_eos())
    return message_tokens


def download_llama_model(repo_id: str, file_name: str) -> Llama:
    snapshot_download(
        repo_id=repo_id,
        local_dir=".",
        allow_patterns=file_name,
    )
    return Llama(
        model_path=file_name,
        n_ctx=2000,
        n_parts=1,
        verbose=True,
    )
