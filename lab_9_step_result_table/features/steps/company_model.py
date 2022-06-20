class CompanyModel(object):
    def __init__(self):
        self.departments={}

    def add_user(self,user_name,dept_name):
        if dept_name not in self.departments:
            self.departments[dept_name]=[]
        
        assert user_name not in self.departments[dept_name]
        self.departments[dept_name].append(user_name)

    def get_headcount_for(self,dept_name):
        return len(self.departments[dept_name])