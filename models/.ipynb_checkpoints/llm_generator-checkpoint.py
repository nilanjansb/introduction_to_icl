import torch
from models.llm_tokenizer import LoadLLM_Model, LoadLLM_Tokenizer
import warnings
warnings.filterwarnings("ignore")

class LLMGenerator:
    def generate(model_name, parameters, prompt : str, gen_mode : bool = False):
        model = parameters['model']
        tokenizer = parameters['tokenizer']
        device = parameters['device']
        enc_tokens = parameters['enc_tokens']
        scores = {}
        inputs = tokenizer([prompt], return_tensors="pt").to(device)

        if gen_mode==False:
            outputs = model.generate(**inputs, do_sample=False,temperature=0.0, top_p=None, top_k=2, return_dict_in_generate=True, output_scores=True, max_new_tokens=1, pad_token_id=2)
            
            score_stack = torch.stack(outputs.scores, dim=1)
    
            current = 0
            if model_name=='zephyr':
                for enc_token in enc_tokens:
                    scores[str(tokenizer.decode(enc_token))] = round(score_stack[0][0][enc_token].item(),3)
                    current+=1
            else:
                for enc_token in enc_tokens:
                    scores[str(tokenizer.decode(enc_token))] = round(score_stack[0][0][enc_token].item(),3)
                    current+=1
                    
            return scores

        else:
            if model_name=='zephyr':
                generated_ids = model.generate(**inputs, max_new_tokens=200)
                gen_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
                return gen_text
            else:
                generated_ids = model.generate(**inputs)
                gen_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
                return gen_text