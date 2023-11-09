from transformers import BartForConditionalGeneration, AutoTokenizer
import torch


class Summarizer:
    def __init__(self) -> None:
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model_checkpoint = "thdangtr/bart-fineturned-on-15-percents-xsum"
        self.model = BartForConditionalGeneration.from_pretrained(
            self.model_checkpoint).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_checkpoint)

    def tokenize(self, input):
        tokenized_input = self.tokenizer(
            input, max_length=512, truncation=True, return_tensors='pt')
        return tokenized_input

    def inference(self, input):
        tokenized_input = self.tokenize(input).to(self.device)
        self.model.eval()
        with torch.no_grad():
            output = self.model.generate(**tokenized_input, max_new_tokens=32)
        summary = self.tokenizer.decode(
            output.squeeze(), skip_special_tokens=True)
        return summary
