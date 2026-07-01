
request_link= lambda year,month,day,report_id:f'https://arquivos.b3.com.br/bdi/download/bdi/{year}-{month}-{day}/{report_id}_{year}{month}{day}.pdf'

map_reports={
    'market_summary':'BDI_02-1'
    }



def request_report(date="yyyy-mm-dd",report_name='market_summary'):
    import requests,os

    report_id=map_reports[report_name]
    year,month,day=[str(i).zfill(2) for i in date.split('-')]
    
    url=request_link(year,month,day,report_id=report_id)

    save_path=f'./data_lake/{report_name}/{os.path.basename(url)}'

    url=request_link(year,month,day,report_id=report_id)
    response = requests.get(url)

    with open(save_path, "wb") as f:
        f.write(response.content)







