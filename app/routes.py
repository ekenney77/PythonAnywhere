from app import app, db, openings
from flask import render_template, redirect, flash, url_for, Blueprint, request
from app.forms import SearchForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return redirect(url_for('search'))
    # return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    search_results=[]
    numMarketing = len(list(db.openings.find({"$text": {"$search": 'marketing'}})))
    numEngineer = len(list(db.openings.find({"$text": {"$search": 'engineer'}})))
    numSales = len(list(db.openings.find({"$text": {"$search": 'sales'}})))
    if form.validate_on_submit():
        search_results = list(db.openings.find({"$text": {"$search": form.search.data}}))
        num_results = len(search_results)
        return render_template('search_results.html', form=form, results=search_results[:10], start=0, end=10, page=1, total=2, q=form.search.data, num_results=num_results)
    return render_template('search.html', numMarketing=numMarketing, numEngineer=numEngineer, numSales=numSales, form=form)


# @app.route('/search3', methods=['GET', 'POST'])
# def search3():
#     form = SearchForm()
#     search_results=[]
#     numMarketing = len(list(db.openings.find({"$text": {"$search": 'marketing'}})))
#     numEngineer = len(list(db.openings.find({"$text": {"$search": 'engineer'}})))
#     numSales = len(list(db.openings.find({"$text": {"$search": 'sales'}})))
#     if form.validate_on_submit():
#         search_results = list(db.openings.find({"$text": {"$search": form.search.data}}))
#         num_results = len(search_results)
#         return render_template('search_results.html', title='Home', form=form, results=search_results[:10], start=0, end=10, page=1, total=2, q=form.search.data, num_results=num_results)
#     return render_template('search3.html', numMarketing=numMarketing, numEngineer=numEngineer, numSales=numSales, form=form)

@app.route('/search_results', methods=['GET', 'POST'])
def search_results():
    form = SearchForm()
    search_results=[]
    if form.validate_on_submit():
        search_results = list(db.openings.find({"$text": {"$search": form.search.data}}))
        num_results = len(search_results)
        return render_template('search_results.html', title='Home', form=form, results=search_results[:10], start=0, end=10, page=1, total=2, q=form.search.data, num_results=num_results)
    per_page = 10
    offset = 0
    page = request.args.get('page', 1, type=int)
    query = request.args.get('q')
    search_results = list(db.openings.find({"$text": {"$search": query}}))
    total = len(search_results)
    t_pages = total // per_page
    start = offset + ((page-1) * per_page)
    end = start + per_page
    results = search_results[start:end]
    num_results = len(search_results)
    return render_template('search_results.html', title='Home', form=form, results=results, page=page, total=t_pages, q=query, start=start, end=end, num_results=num_results)

@app.route('/job/<posting>', methods=['GET', 'POST'])
def job_post(posting):
    form = SearchForm()
    search_results=[]
    if form.validate_on_submit():
        search_results = list(db.openings.find({"$text": {"$search": form.search.data}}))
        num_results = len(search_results)
        return render_template('search_results.html', title='Home', form=form, results=search_results[:10], start=0, end=10, page=1, total=2, q=form.search.data, num_results=num_results)
    title_dict = db.openings.find_one({'Id': posting}, {'Title': 1, '_id':0})
    if title_dict is None:
        return render_template('404.html', form=form), 404
    title = ''
    for i in title_dict:
        title += title_dict[i]
    date_dict = db.openings.find_one({'Id': posting}, {'Date': 1, '_id':0})
    date = ''
    for i in date_dict:
        date += date_dict[i]
    company_dict = db.openings.find_one({'Id': posting}, {'Company': 1, '_id':0})
    company = ''
    for i in company_dict:
        company += company_dict[i]
    description_dict = db.openings.find_one({'Id': posting}, {'Description': 1, '_id':0})
    description = ''
    for i in description_dict:
        description += description_dict[i]
    link_dict = db.openings.find_one({'Id': posting}, {'Link': 1, '_id':0})
    link = ''
    for i in link_dict:
        link += link_dict[i]
    return render_template('post_page.html', form=form, posting=posting, title=title, date=date, company=company, description=description, link=link)

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = SearchForm()
    search_results=[]
    if form.validate_on_submit():
        search_results = list(db.openings.find({"$text": {"$search": form.search.data}}))
        num_results = len(search_results)
        return render_template('search_results.html', title='Home', form=form, results=search_results[:10], start=0, end=10, page=1, total=2, q=form.search.data, num_results=num_results)
    return render_template('about.html', form=form)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = SearchForm()
    search_results=[]
    if form.validate_on_submit():
        search_results = list(db.openings.find({"$text": {"$search": form.search.data}}))
        num_results = len(search_results)
        return render_template('search_results.html', title='Home', form=form, results=search_results[:10], start=0, end=10, page=1, total=2, q=form.search.data, num_results=num_results)
    return render_template('submit.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    form = SearchForm()
    search_results=[]
    if form.validate_on_submit():
        search_results = list(db.openings.find({"$text": {"$search": form.search.data}}))
        num_results = len(search_results)
        return render_template('search_results.html', title='Home', form=form, results=search_results[:10], start=0, end=10, page=1, total=2, q=form.search.data, num_results=num_results)
    return render_template('404.html', form=form), 404
