import part1

from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'project'


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/ops')
def list_of_ops_page():
    return render_template('ops.html')


@app.route('/num_row_page')
def num_row_3():
    result = part1.coordinator().num_row_1('number of rows')
    return render_template('num_row_page.html', result=result)


@app.route('/num_col_page')
def num_col_3():
    result = part1.coordinator().num_col_1('number of columns')
    return render_template('num_col_page.html', result=result)


@app.route('/labels_of_col_page')
def label_df_3():
    result = part1.coordinator().labels_df_1('labels of columns')
    return render_template('labels_of_col_page.html', result=result)


@app.route('/gene_each_biotype_page')
def gene_each_biotype_3():
    result = part1.coordinator().genes_each_biotype_1('gene each biotype')
    return render_template('gene_each_biotype_page.html', result=result)

@app.route('/certain_biotype_page', methods=['GET','POST'])
def certain_biotype_3():
    if request.method=='GET':
        return render_template('certain_biotype_page.html')
    else:
        biotype = request.form['biotype']
        ress= part1.coordinator().certain_biotype_1('certain biotype',biotype)
        return render_template('certain_biotype_page.html', result=ress)

@app.route('/num_chr_page')
def num_chr_3():
    result = part1.coordinator().num_chr_1('number of chromosomes')
    return render_template('num_chr_page.html', result=result)

@app.route('/gene_each_chr_page')
def gene_each_chr_3():
    result = part1.coordinator().genes_each_chr_1('gene each chromosome')
    return render_template('gene_each_chr_page.html', result=result)

@app.route('/gene_on_p_page')
def gene_on_p():
    result = part1.coordinator().gene_on_p('gene on + strand')
    return render_template('gene_on_p_page.html', result=result)

@app.route('/gene_on_m_page')
def gene_on_m():
    result = part1.coordinator().gene_on_m('gene on - strand')
    return render_template('gene_on_m_page.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
