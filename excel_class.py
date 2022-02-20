class ExcelSorts:




    def sum_of_rows(self, df, row_name):
        sum_df = df[row_name].sum()
        return sum_df


    def sorted_rows (self, df, row_name):

         df = df.dropna()
         return df.sort_values(by=[row_name], ascending=True)

    def reverse_sort_rows(self, df, row_name):
        reverse_sorted_df = df.sort_values(by=[row_name], ascending=False)
        return reverse_sorted_df

