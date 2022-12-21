from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Program:
    db_name='university'
    def __init__(self,data):
        self.id = data['id'],
        self.programname = data['programname'],
        self.universityname = data['universityname'],
        self.universitylocation = data['universitylocation'],        
        self.fieldofstudy = data['fieldofstudy'],
        self.educationlevel = data['educationlevel'],
        self.requirements = data['requirements'],
        self.description = data['description'],
        self.language = data['language'],
        self.tuitionfee = data['tuitionfee'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
   
    @classmethod
    def getAllPrograms(cls):
        query = 'SELECT * FROM universityprograms;'
        results = connectToMySQL(cls.db_name).query_db(query)
        programs = []
        for row in results:
            programs.append(row)
        return programs
    
    @classmethod
    def createProgram(cls,data):
        query = 'INSERT INTO universityprograms (programname,universityname,universitylocation,fieldofstudy,educationlevel,requirements,description,language,tuitionfee, users_id) VALUES(%(programname)s,%(universityname)s,%(universitylocation)s,%(fieldofstudy)s,%(educationlevel)s,%(requirements)s,%(description)s,%(language)s,%(tuitionfee)s, %(users_id)s);'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_program_by_id(cls,data):
        query = 'SELECT * FROM universityprograms WHERE id = %(program_id)s ;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]
    
    @classmethod
    def update_program(cls,data1):
        query = 'UPDATE universityprograms SET programname=%(programname)s, universityname=%(universityname)s, universitylocation=%(universitylocation)s,fieldofstudy=%(fieldofstudy)s,educationlevel=%(educationlevel)s,requirements=%(requirements)s,description=%(description)s,language=%(language)s,tuitionfee=%(tuitionfee)s WHERE id=%(program_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data1)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM universityprograms WHERE id = %(program_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_logged_user_favorite_programs(cls, data):
        query = 'SELECT programs_id  as id FROM favoriteprograms LEFT JOIN users on favoriteprograms.users_id = users.id WHERE users_id = %(user_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        FavoritePrograms = []
        for row in results:
            FavoritePrograms.append(row['id'])
        return FavoritePrograms    

    @classmethod
    def getFavoritePrograms(cls, data):
        query = 'SELECT favoriteprograms.programs_id as id FROM universityprograms LEFT JOIN favoriteprograms on favoriteprograms.programs_id = universityprograms.id WHERE universityprograms.id = %(program_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        FavoritePrograms = []
        for row in results:
            FavoritePrograms.append(row['id'])
        return FavoritePrograms

    @classmethod
    def addtoFav(cls, data):
        query= 'INSERT INTO favoriteprograms (programs_id, users_id) VALUES ( %(program_id)s, %(user_id)s );'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def removefromFav(cls, data):
        query= 'DELETE FROM favoriteprograms WHERE programs_id = %(program_id)s and users_id = %(user_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    
    @staticmethod
    def validate_program(universityprogram):
        is_valid = True
        if len(universityprogram['programname']) < 1:
            flash("All fields are required.", 'empty')
            is_valid = False

        if len(universityprogram['universityname']) < 1:
            flash("All fields are required.", 'empty')
            is_valid = False

        if len(universityprogram['universitylocation']) < 1:
            flash("All fields are required.", 'empty')
            is_valid = False

        if len(universityprogram['fieldofstudy']) < 1:
            flash("All fields are required.", 'empty')
            is_valid = False
        
        if len(universityprogram['educationlevel']) < 1:
            flash("All fields are required.", 'empty')
            is_valid = False

        if len(universityprogram['requirements']) < 1:
            flash("All fields are required.", 'empty')
            is_valid = False

        if len(universityprogram['description']) < 1:
            flash("All fields are required.", 'empty')
            is_valid = False

        if len(universityprogram['language']) < 1:
            flash("All fields are required.", 'empty')
            is_valid = False

        if len(universityprogram['tuitionfee']) < 1:
            flash("All fields are required.", 'empty')
            is_valid = False
        return is_valid