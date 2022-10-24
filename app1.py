#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:22:36 2022

@author: sergey
"""

import uuid
from flask import Flask, render_template, url_for, request, flash, session, redirect
import numpy as np
from tensorflow.keras import models


import pickle

mod_name = 'scaler.pkl'
with open(mod_name , 'rb') as f:
    scaler = pickle.load(f)


model = models.load_model('in_college.h5')


#print(type(model))





app = Flask(__name__)
app.config['SECRET_KEY'] = 'nsdndjngjnnjdasjkwebju5489djkdgjkdjk347hdk'

# Словарь пунктов меню и соответствующих им ссылок
menu = [{'name': 'Ввод нового события', 'url': 'enter_item'},        
        {'name': 'О проекте', 'url': 'about'} ]



# Обработчик главной страницы
@app.route("/")
@app.route("/index")
def index():
    print (url_for('index'))
    return render_template("index.html", title = "Главная страница", menu = menu)

@app.route("/about")
def about():
    return render_template("about.html", title = "о проекте", menu = menu)


# Обработчик формы ввода нового события
# реализует базовые проверки на непустоту полей
@app.route("/enter_item", methods = ['POST', 'GET'])
def enter_item():
    
    
    
    
    if request.method == 'POST':
        pairs = dict(request.form)
        

        flags = {}
        for v in pairs.values():
            flags[v] = False

        for k, v in pairs.items():
            if len(v) < 1:
                s = k + ' incorrect'
                flash(s)
            else:
                flags[v] = True
        
        f = False
        for v in flags.values():
            if v == True:
                f = True


        if f:
        
            #  подготовка вектора V
            v = [] 
            
            for val in pairs.values():
                v.append(float(val))
            
            v = np.array(v)
            v = np.expand_dims(v, axis = 0)
 #           v = np.array(list(pairs.values())).reshape(1, -1)
            
            v = scaler.transform(v)
            
            print (v)
            if model.predict(v) > 0.5:
                flash('поступишь')
            else:
                flash('иди мыть полы')
            

        else:
            print ('чего-то не хватило')

        
        
        '''
        
        file = request.files['fotofile']
        
        if file.filename == '' and len(request.form['fotolink']) < 4:
            flash('Нет данных об изображении!')
        else:
            pi = True
            
            
        # Если есть картинка, то ее сохраняю в папочку 
        # в pairs добавляю имя файла для сохранения в таблицу 
        
        if file.filename != '':
            
            filename = 'images/'+str(uuid.uuid4())+'.'+file.filename.split('.')[-1]
            file.save(filename)
            
            pairs['fotofile'] = filename
        # закончил сохранять картинку            
        
        
        
        
        if len(request.form['Par_1']) < 1:
            flash('Название не введено!')
        else:
            f1 = True
        if len(request.form['Par_2']) < 1:
            flash('Категория не введена!')
        else:
            f2 = True

        if len(request.form['Par_3']) < 1:
            flash('Подкатегория не введена!')
        else:
            f3 = True
            
        if len(request.form['Par_4']) < 1:
            flash('Дата не введена!')
        else:
            f4 = True
        if len(request.form['par_5']) < 1:
            flash('Ссылка на афишу не введена!')
        else:
            f5 = True
        if len(request.form['descant']) < 1:
            flash('Описание не введено!')
        else:
            de = True
      
        if (na*ty*sty*al*de*dt*pi):
            pass
        else:
            print ('чего-то не хватило')
        '''    
        return render_template("enter_item.html", title = "новый прогноз", menu = menu)    
    else:
        return render_template("enter_item.html", title = "новый прогноз", menu = menu)


if __name__ == '__main__':
    app.run(debug=True)


