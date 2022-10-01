from transformers import GPT2LMHeadModel, PreTrainedTokenizerFast

class MakeWords(object):
    def __init__(self):
        self.BOS = "</s>"
        self.EOS = "</s>"
        self.UNK = "<unk>"
        self.PAD = "<pad>"
        self.MASK = "<mask>"

        self.model = GPT2LMHeadModel.from_pretrained("skt/kogpt2-base-v2")
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2", bos_token=self.BOS, eos_token=self.EOS, unk_token=self.UNK, pad_token=self.PAD, mask_token=self.MASK)

    def tokenize(self, text):
        return self.tokenizer.encode(text, return_tensors="pt")

    def generate(self, tokens):
        return self.model.generate(tokens,max_length=256,repetition_penalty=2.0, pad_token_id=self.tokenizer.pad_token_id, eos_token_id=self.tokenizer.eos_token_id, bos_token_id=self.tokenizer.bos_token_id, use_cache=True)

    def create(self, text):
        input_token_ids = self.tokenize(text)

        gen_ids = self.generate(input_token_ids)        

        generated = self.tokenizer.decode(gen_ids[0])

        return generated


if __name__ == "__main__":
    creator = MakeWords()

    print(creator.create("종교도 철학적 사색에 빛을 줄 수 있다. 철학적 사색은 종교적 진리 를 확실하게 할 수 있다. 그러므로 살아 있든 죽어 있든 간에 진실한 종교인, 참된 철학인과 교제를 청하라."))