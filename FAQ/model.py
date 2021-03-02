from tensorflow.keras import Model
from transformers import TFBertModel
import os
# bert_modle = r'E:\dialogue system\CarDialogueSystem\bert_ch'

path = os.path.dirname(__file__).split('/')[:-1]
newpath = '/'.join(path)
bert_modle = os.path.join(newpath, 'bert_ch')


class car_aq_model(Model):
    def __init__(self):
        super(car_aq_model, self).__init__()
        self.Bert_Model = TFBertModel.from_pretrained(bert_modle)

    def call(self, input_ids, token_type_ids, attention_mask):
        outputs = self.Bert_Model([input_ids, token_type_ids, attention_mask])
        # sentence_vector = outputs[0][-2][0][0]
        # for each_vector in outputs[0][-2][0]:
        #     sentence_vector = sentence1_vector + each_vector

        sentence_vector = outputs[0][0][0]
        return sentence_vector
