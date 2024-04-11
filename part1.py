import pandas as pd
import part2
import part3

class reader():
    Df = pd.read_csv("data_set.txt", delimiter=",")
    ops = {'number of rows': part2.dataFrame(Df), 'number of columns': part2.dataFrame(Df), 'labels of columns':
                    part2.dataFrame(Df),'gene each biotype':part2.dataFrame(Df),'certain biotype':part2.dataFrame(Df),
           'number of chromosomes':part2.dataFrame(Df), 'gene each chromosome':part2.dataFrame(Df), 'gene on + strand':
           part2.dataFrame(Df), 'gene on - strand':part2.dataFrame(Df)}

class coordinator(reader):

    def num_row_1(self, operationKey):
        if operationKey=='number of rows':
            num_rows_1= self.ops[operationKey].num_row_2()
            return num_rows_1

    def num_col_1(self, operationKey):
        if operationKey == 'number of columns':
            num_columns_1 = self.ops[operationKey].num_col_2()
            return num_columns_1

    def labels_df_1(self, operationKey):
        if operationKey == 'labels of columns':
            labels_df_1=self.ops[operationKey].labels_df_2()
            return labels_df_1

    def genes_each_biotype_1(self, operationKey):
        if operationKey == 'gene each biotype':
            genes_each_biotype_1=self.ops[operationKey].gene_each_biotype_2()
            return genes_each_biotype_1

    def certain_biotype_1(self, operationKey,biotype):
        if operationKey == 'certain biotype':
            certain_biotype_1=self.ops[operationKey].certain_biotype_2(biotype)
            return certain_biotype_1

    def num_chr_1(self, operationKey):
        if operationKey == 'number of chromosomes':
            num_chr_1=self.ops[operationKey].num_chr_2()
            return num_chr_1

    def genes_each_chr_1(self, operationKey):
        if operationKey == 'gene each chromosome':
            genes_each_chr_1=self.ops[operationKey].gene_each_chr_2()
            return genes_each_chr_1

    def gene_on_p(self, operationKey):
        if operationKey== 'gene on + strand':
            gene_on_p=self.ops[operationKey].gene_on_p()
            return gene_on_p

    def gene_on_m(self, operationKey):
        if operationKey== 'gene on - strand':
            gene_on_m=self.ops[operationKey].gene_on_m()
            return gene_on_m

if __name__ == "__main__":
    Coordinator = coordinator()
    Coordinator.num_row_1('number of rows')
    Coordinator.num_col_1('number of columns')
    Coordinator.labels_df_1('labels of columns')
    Coordinator.genes_each_biotype_1('gene each biotype')
    Coordinator.certain_biotype_1('certain biotype',part3.certain_biotype_3())
    Coordinator.num_chr_1('number of chromosomes')
    Coordinator.genes_each_chr_1('gene each chromosome')
    Coordinator.gene_on_p('gene on + strand')
    Coordinator.gene_on_m('gene on - strand')