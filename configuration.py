import os

# Current working directory
cwd = os.getcwd()

# passage index location
index_path = '/home/21cd92r02/Documents/Nilanjan/DataStore/index/'

# path to models cache
cache_path = '/home/21cd92r02/Documents/cache/'

# dataset_configuration
datasets = {
    'msmarco_passage':{
            'name':'msmarco_passage',
            'topics': 'train',
            'index':f'{index_path}trecdl_index'
        },
    'dl19':{
            'name':'irds:msmarco-passage/trec-dl-2019/judged',
            'topics': 'text',
            'index':f'{index_path}trecdl_index'
        }
}

rerankers = {
    'zephyr':{
            'model_name':'HuggingFaceH4/zephyr-7b-beta',
            'tokenizer': 'HuggingFaceH4/zephyr-7b-beta'
        },
    'flanxl':{
            'model_name':'google/flan-t5-xl',
            'tokenizer': 'google/flan-t5-xl'
        }
}
