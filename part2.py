from abc import ABC, abstractclassmethod
import numpy as np

class abstractClass(ABC):

    @abstractclassmethod
    def num_row_2(self):
        pass
    @abstractclassmethod
    def num_col_2(self):
        pass
    @abstractclassmethod
    def labels_df_2(self):
        pass

    @abstractclassmethod
    def gene_each_biotype_2(self):
        pass

    @abstractclassmethod
    def certain_biotype_2(self,biotype):
        pass

    @abstractclassmethod
    def num_chr_2(self):
        pass

    @abstractclassmethod
    def gene_each_chr_2(self):
        pass

    @abstractclassmethod
    def gene_on_p(self):
        pass

    @abstractclassmethod
    def gene_on_m(self):
        pass

class dataFrame(abstractClass):
    def __init__(self, df):

        self._df = df

    def num_row_2(self):
        return self._df.shape[0]

    def num_col_2(self):
        return self._df.shape[1]

    def labels_df_2(self):
        return self._df.head(0)

    def gene_each_biotype_2(self):
        res= self._df.groupby('gene_biotype').size()
        return dict(res.sort_values(ascending=True))

    def certain_biotype_2(self,biotype):
        res = self._df.loc[self._df['gene_biotype'] == biotype ,  'gene_name']
        return dict(res)

    def num_chr_2(self):
        res=self._df.chromosome.nunique(dropna = True)
        return res

    def gene_each_chr_2(self):
        res= self._df.groupby('chromosome').size()
        return dict(res.sort_values(ascending=True))

    def gene_on_p(self):
        res = self._df.loc[self._df['strand'] == '+', 'chromosome']
        ress = res.value_counts(normalize=True).map("{:.3%}".format)
        return dict(ress)

    def gene_on_m(self):
        res = self._df.loc[self._df['strand'] == '-', 'chromosome']
        ress = res.value_counts(normalize=True).map("{:.3%}".format)
        return dict(ress)