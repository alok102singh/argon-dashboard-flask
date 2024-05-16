# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - present CDNX Texhnologies
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps import db, login_manager
from apps.home.models import Grade, Section, BloodGroup, Religious, Student
from flask import render_template, redirect, request, url_for


@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')


@blueprint.route('/grade')
@login_required
def grade():
    grades = Grade.query.all()
    return render_template('home/grade.html', segment='grade', grades=grades)


@blueprint.route('/add_grade', methods=['POST', 'GET'])
@login_required
def add_grade():
    if request.method == 'POST':
        grade = request.form['grade']
        status = request.form['status']
        new_grade = Grade(grade=grade, status=status)
        db.session.add(new_grade)
        db.session.commit()
        return redirect(url_for('home_blueprint.grade'))
    else:
        return render_template('home/add_grade.html', segment='grade')


@blueprint.route('/section')
@login_required
def section():
    sections = Section.query.all()
    return render_template('home/section.html', segment='section', sections=sections)


@blueprint.route('/add_section', methods=['POST', 'GET'])
@login_required
def add_section():
    if request.method == 'POST':
        section = request.form['section']
        status = request.form['status']
        grade_id = request.form['grade']
        new_section = Section(section=section, status=status, grade_id=grade_id)
        db.session.add(new_section)
        db.session.commit()
        return redirect(url_for('home_blueprint.section'))
    else:
        grades = Grade.query.all()
        return render_template('home/add_section.html', segment='section', grades=grades)


@blueprint.route('/blood_group')
@login_required
def blood_group():
    list = BloodGroup.query.all()
    return render_template('home/blood_group.html', segment='blood_group', list=list)


@blueprint.route('/add_blood_group', methods=['POST', 'GET'])
@login_required
def add_blood_group():
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        item = BloodGroup(name=name, status=status)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('home_blueprint.blood_group'))
    else:
        return render_template('home/add_blood_group.html', segment='blood_group')


@blueprint.route('/religious')
@login_required
def religious():
    list = Religious.query.all()
    return render_template('home/religious.html', segment='religious', list=list)


@blueprint.route('/add_religious', methods=['POST', 'GET'])
@login_required
def add_religious():
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        item = Religious(name=name, status=status)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('home_blueprint.religious'))
    else:
        return render_template('home/add_religious.html', segment='religious')


@blueprint.route('/student')
@login_required
def student():
    list = Student.query.all()
    return render_template('home/student.html', segment='student', list=list)


@blueprint.route('/add_student', methods=['POST', 'GET'])
@login_required
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        father_mobile = request.form['father_mobile']
        mother_mobile = request.form['mother_mobile']
        address1 = request.form['address1']
        address2 = request.form['address2']
        city = request.form['city']
        state = request.form['state']
        dob = request.form['dob']
        pin_code = request.form['pin_code']
        status = request.form['status']
        item = Student(name=name, father_name=father_name, mother_name=mother_name, father_mobile=father_mobile,
                       mother_mobile=mother_mobile, address1=address1, address2=address2, city=city, state=state,
                       pin_code=pin_code, dob=dob,
                       status=status)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('home_blueprint.student'))
    else:
        grades = Grade.query.all()
        grades = Grade.query.all()
        grades = Grade.query.all()
        grades = Grade.query.all()
        return render_template('home/add_student.html', segment='student')
