import re
import itertools
import pprint


class BasicCipher(object):
    """ 
    Transposed Cipher,
    Works to decrypt GCHQ encryption challenge.
    """
    def __init__(self):
        self.word = '''
            AWVLI QIQVT QOSQO ELGCV IIQWD LCUQE EOENN WWOAO
            LTDNU QTGAW TSMDO QTLAO QSDCH PQQIQ DQQTQ OOTUD
            BNIQH BHHTD UTEET FDUEA UMORE SQEQE MLTME TIREC
            LICAI QATUN QRALT ENEIN RKG'''
        self.word = re.sub(r'\s+', '', self.word)
        self.word = list(self.word)

    
    def __len__(self):
        return len(self.word)

    
    def factors(self):
        """
        Find all factors of a number.
        """
        return [x for x in range(2, len(self)//2+1) if len(self)%x == 0]

    
    def split_seq(self, iterable, size):
        """
        give the ability to split the item with any size
        [[a, a, a],
        [a, a, a],
        [a, a, a]]

        splitted by the factor 3.

        """
        it = iter(iterable)
        item = list(itertools.islice(it, size))
        while item:
            yield item
            item = list(itertools.islice(it, size))
     
    
    def _result(self):
        """ Get a list splitted, then join it in the vertical.
        [[b, b, b],
        [a, c, d],
        [c, u, z]],

        bac bcu bdz

        """
        table = list(self.split_seq(self.word, self.factors()[1]))
        newl = zip(*table)

        #replace letter 'Q' with space or dot
        #comparing to english frequency letter this letter is not used so often.
        plaintext = ''.join(x for xs in newl for x in xs).replace('Q', '.')
        pprint.pprint(plaintext)
    
    
if __name__ == '__main__':
    b = BasicCipher()
    b._result()
