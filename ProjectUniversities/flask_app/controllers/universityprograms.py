from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.universityprogram import Program
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/addProgram')
def addprogram():
    if 'user_id' not in session:
            return redirect('/logout')
    data={
        'user_id': session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('addProgram.html',loggedUser= User.get_user_by_id(data))

@app.route('/createprogram', methods = ['POST'])
def create_program():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Program.validate_program(request.form):
        return redirect(request.referrer)
    Program.createProgram(request.form)
    return redirect('/')

@app.route('/browse')
def browse():
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'user_id': session['user_id']
    }
    universityprograms = Program.getAllPrograms()
    user = User.get_user_by_id(data)
    
    return render_template('browsePrograms.html',loggedUser= User.get_user_by_id(data), universityprograms=universityprograms)

@app.route('/showUni/<int:id>')
def viewProgram(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'program_id': id,
        'user_id': session['user_id']
    }
    userFavoritePrograms = Program.get_logged_user_favorite_programs(data)
    return render_template('showUni.html', loggedUser= User.get_user_by_id(data), program = Program.get_program_by_id(data), userFavoritePrograms=userFavoritePrograms)

@app.route('/addtoFav/<int:id>')
def addFavorite(id):
    data = {
        'program_id': id,
        'user_id': session['user_id']
    }
    Program.addtoFav(data)
    return redirect(request.referrer)

@app.route('/removefromFav/<int:id>')
def removeFavorite(id):
    data = {
        'program_id': id,
        'user_id': session['user_id']
    }
    Program.removefromFav(data)
    return redirect(request.referrer)

@app.route('/myPrograms')
def showfavorites():
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'program_id': id,
        'user_id': session['user_id']
    }
    universityprograms = Program.getAllPrograms()
    favprograms = Program.getFavoritePrograms(data)
    user = User.get_user_by_id(data)
    
    return render_template('myFavoritePrograms.html',loggedUser= User.get_user_by_id(data), universityprograms=universityprograms, favprograms=favprograms)