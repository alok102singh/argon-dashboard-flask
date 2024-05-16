# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - present CDNX Texhnologies
"""
from datetime import datetime

from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass


class Grade(db.Model):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)


class Section(db.Model):
    __tablename__ = 'sections'

    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    grade_id = db.Column(db.Integer, db.ForeignKey('grades.id'), nullable=False)
    grade = db.relationship('Grade', backref=db.backref('sections', lazy=True))


class BloodGroup(db.Model):
    __tablename__ = 'blood_group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)


class Religious(db.Model):
    __tablename__ = 'religious'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    mother_name = db.Column(db.String(100), nullable=False)
    father_mobile = db.Column(db.String(15), nullable=False)
    mother_mobile = db.Column(db.String(15), nullable=False)
    address1 = db.Column(db.String(200), nullable=False)
    address2 = db.Column(db.String(200))
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    pin_code = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.Date, nullable=False)

    blood_group_id = db.Column(db.Integer, db.ForeignKey('blood_group.id'), nullable=False)
    blood_group = db.relationship('BloodGroup')

    religious_id = db.Column(db.Integer, db.ForeignKey('religious.id'), nullable=False)
    religious = db.relationship('Religious')

    grade_id = db.Column(db.Integer, db.ForeignKey('grades.id'), nullable=False)
    grade = db.relationship('Grade')

    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'), nullable=False)
    section = db.relationship('Section')
    created_by = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
