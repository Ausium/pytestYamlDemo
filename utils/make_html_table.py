

def make_html_table(title,header,content):
    table_msg = '<table border="1" bordercolor="#c8c9cc"; cellpadding="7" cellspacing="0"; style="table-layout: fixed; font-size:14px;width: 1200px;border-collapse: collapse;">'
        
    
    table_msg += '<colgroup>'
    colspan_num = 0
    for col in header:
        colspan_num += 1
        if col == '接口响应结果':
            table_msg += '<col style="width: 40%;">'
        else:
            table_msg += '<col>'
    table_msg += '</colgroup>'

    table_title = '<tr><td colspan="%s" style="padding: 15px;font-weight:bold"\
        font-size:18px;padding-bottom:16px">%s</td>\
        </tr>' % (colspan_num,title)

    table_header = '<tr>'
    for item in header:
        table_header += '<td style="padding: 10px;text-align: center; background-color: #e1e4eb; border: 1px solid #ccc;font-weight:bold;">%s\
        </td>' % (item)
    table_header += '</tr>'
    
    table_content = ''
    for item in content:
        table_content += '<tr>'
        for value in item:
            table_content += '<td style="text-align: center;padding: 10px; border: 1px solid #ccc;word-break: break-all;">%s</td>' % (value)
        table_content += '</tr>'
    table_content += '</table>'

    return table_msg + table_title + table_header + table_content + '<br>'