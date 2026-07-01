from pandas import read_excel
def format_(ref_data='yymm'):
 
    data_path=f'./data_lake/sectoral_classification/{ref_data}_SectoralClassif.xlsx'
    save_path=f"./data_lake_organized/ticket_dimension/{ref_data}_sectoral_classification.csv"
    
    base=read_excel(data_path)
    #drop nan columns
    useful_cols=((base.isna()==False).sum()>0)[((base.isna()==False).sum()>0)].index
    base=base[useful_cols]

    #rename columns
    header_1_id=base.iloc[:,1].notna().index[0]
    header_2_id=header_1_id+1
    column_names = [ i if str(i)!='nan' else j for i,j in zip(base.iloc[header_1_id],base.iloc[header_2_id])      ]
    base.columns=column_names

    #remove header_lines
    base=base.drop(index=[header_1_id,header_2_id])
    
    header_line=(
        base.apply(lambda row:
                sum( [ row[col_i]==col_i for col_i in base.columns]),
                axis=1)==0)
    base=base[header_line]

    # preencher dados
    base=base.ffill()

    base.to_csv(save_path,sep=';',decimal=',')
    