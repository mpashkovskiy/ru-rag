# ru-rag

[English version of the documentation](#in-english)

Пример реализации генерации дополненной извлечением (Retrieval Augmented Generation, RAG) для русского языка.

## Системные требования

- Python 3.9;
- Для получения краткого содержания желательно наличие графической карты (GPU). Тем не мение, код исполняется и на обычном процессоре (CPU). Время генерации:
  - MacBook Pro 13', M2, 2022 - порядка 20 минут;
  - AWS g5.4xlarge EC2 сервер - порядка одной минуты.

## Использование

- Выполните одно из двух:
  - `pip install git+https://github.com/mpashkovskii/ru-rag.git` для установки модуля;
  - или склонируйте репозиторий, выполните `make install` в папке и потом активируйте виртуальное окружение командой `source .venv/bin/activate`;
- Поместите CSV файлы датасета в папку `data`. Пример файла: [dataset_example.csv](dataset_example.csv);
  - файлы должны иметь расширение `.csv`;
  - в файлах должен присутсвовать заголовок - имена колонок;
  - в файлах должна присутсвовать колонка `text`;
  - значения должны быть разделеный табуляцией;
- Инициализируйте базу данных командой `populate_db`;
- Для поиска релевантных данных используйте команду `find_similar "Что такое арбуз?"`;
- Для поиска релевантных данных и получения краткого ответа используйте команду `answer "Что такое арбуз?"`;
- Основной код расположен в [ru_rag/serve.py](ru_rag/serve.py);

## Лицензия

Код распространяется по лицензии [Attribution 4.0 International (CC BY 4.0)](LICENSE): можно модифицировать и использовать при условии что будет указано авторство и ссылка на этот репозиторий.

## Ссылки

- Для эмбединга используется модель [sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2);
- Для RAG - [IlyaGusev/saiga_13b_lora_llamacpp](https://huggingface.co/IlyaGusev/saiga_13b_lora_llamacpp);
- RAG код частично позаимствован из [Saiga 13B llama.cpp: retrieval QA](https://huggingface.co/spaces/IlyaGusev/saiga_13b_llamacpp_retrieval_qa) выполненого [Ильей Гусевым](https://github.com/IlyaGusev);
- [Buy me a coffee](https://bmc.link/mpashkovskii).

## In English

RAG pipeline implementation example for the Russian language.

### System requirements

- Python 3.9;
- GPU is recommended but the code also works on CPU. Generation time:
  - MacBook Pro 13', M2, 2022 - approx. 20 minutes;
  - AWS g5.4xlarge EC2 machine - approx. one minute.

### Usage

- Either:
  - execute `pip install pip@git+https://github.com/mpashkovskii/ru-rag.git` to install the package;
  - or clone the repo, run `make install` in the folder, and `source .venv/bin/activate` to activate the virtual environment;
- Put dataset CSV files in `data` directory. CSV file example: [dataset_example.csv](dataset_example.csv).
  - files have to have `.csv` extension;
  - files have to have a header consisting of column names;
  - `text` column has to be presented in the files;
  - values are separated with tabulation;
- Populate the database with `populate_db` command;
- To find similar documents use `find_similar "Что такое арбуз?"` command;
- To get summary and source documents use `answer "Что такое арбуз?"` command;
- See [ru_rag/serve.py](ru_rag/serve.py) for more details.

## License

The code is under [Attribution 4.0 International (CC BY 4.0)](LICENSE):

You are free to:

- Share — copy and redistribute the material in any medium or format;
- Adapt — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:

- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use;
- No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

## Links

- Embedding model: [sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2);
- LLM model: [IlyaGusev/saiga_13b_lora_llamacpp](https://huggingface.co/IlyaGusev/saiga_13b_lora_llamacpp);
- RAG code is partially taken from [Saiga 13B llama.cpp: retrieval QA](https://huggingface.co/spaces/IlyaGusev/saiga_13b_llamacpp_retrieval_qa) build by [Ilya Gusev](https://github.com/IlyaGusev);
- [Buy me a coffee](https://bmc.link/mpashkovskii).
