class NameFromEmail:

    def solution(self):

        email = "ashik@gmail.com"

        index_of_at = email.rfind("@")

        return email[:index_of_at]
    
name_from_email_instance = NameFromEmail()

print(name_from_email_instance.solution())