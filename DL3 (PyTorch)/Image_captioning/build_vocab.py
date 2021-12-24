# build_vocab.py

import nltk
nltk.download('punkt') # nltk 사용을 위해 설치
import pickle
import argparse
from collections import Counter
from pycocotools.coco import COCO

class Vocabulary(object):
    """simple vocabulary wrapper."""
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0

    def add_word(self, word):
        if not word in self.word2idx:
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1

    def __call__(self, word):
        if not word in self.word2idx:
            return self.word2idx['<unk>']
        return self.word2idx[word]

    def __len__(self):
        return len(self.word2idx)


def build_vocab(json, threshold):
    """build a simple vocabulary wrapper."""
    coco = COCO(json)
    counter = Counter() # list안의 단어의 출현 빈도 dict로 반환
    ids = coco.anns.keys() # 그림에 대한 annotations

    for i, id in enumerate(ids):
        caption = str(coco.anns[id]['caption'])
        tokens = nltk.tokenize.word_tokenize(caption.lower())

    if (i+1)%1000==0:
        print(f'[{i+1}/{len(ids)}] Tokenized the captions.')
    
    # if the wod frequency is less than 'threshold', then the word is discarded.
    words = [word for word, cnt in counter.items() if cnt >= threshold]

    # create a vocab wrapper and add some special tokens.
    vocab = Vocabulary()
    vocab.add_word('<pad>')
    vocab.add_word('<sos>')
    vocab.add_word('<eos>')
    vocab.add_word('<unk>')

    # add the words to the vocabulary.
    for i, word in enumerate(words):
        vocab.add_word(word)

    return vocab

def main(args):
    vocab = build_vocab(json=args.caption_path, threshold=args.threshold)
    vocab_path = args.vocab_path

    with open(vocab_path, 'wb') as f:
        pickle.dump(vocab, f)

    print(f'Total vocabulary size {len(vocab)}')
    print(f'Saved the vocabulary wrapper to {vocab_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--caption_path', type=str, 
                        default='data/annotations/captions_train2014.json', 
                        help='path for train annotation file')
    parser.add_argument('--vocab_path', type=str, default='./data/vocab.pkl', 
                        help='path for saving vocabulary wrapper')
    parser.add_argument('--threshold', type=int, default=4, 
                        help='minimum word count threshold')
    args = parser.parse_args()
    main(args)