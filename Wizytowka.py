from faker import Faker
import random


fak = Faker("pl_PL")


# W związku z tym, że dane będą po polsku, to czasem trzeba będzie usunąć polskie znaki:
def normalize_letters(tekst):
    text = tekst.lower()
    polish_letters = "ąćęłńóśźż"
    normal_letters = "acelnoszz"
    new_text = ""
    for i in text:
        letter = i
        if letter in polish_letters:
            letter = normal_letters[polish_letters.index(i)]
        new_text += letter
    return new_text

    # Tutaj stworzyłem funkcje, które generują fałszywe dane osobowe:.......................................................


def fakemail(firstname, lastname):
    norm_firstname = normalize_letters(firstname)
    norm_lastname = normalize_letters(lastname)
    mail_domain = fak.domain_name()
    bizmail = f"{norm_firstname}.{norm_lastname}@{mail_domain}"
    return bizmail


def random_npc():
    firstname = fak.first_name()
    lastname = fak.last_name()
    privtel = fak.phone_number()
    biztel = fak.phone_number()
    mail = fakemail(firstname, lastname)
    job = fak.job()
    return [firstname, lastname, privtel, mail, biztel, job]


# Tutaj jest główna klasa, wizytówka:.....................................................................................
class BaseContact:
    def __init__(self, firstname, lastname, tel, mail):
        self.firstname = firstname
        self.lastname = lastname
        self.tel = tel
        self.mail = mail

        # Variables:
        self._label_length = len(self.firstname)+len(self.lastname)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname} {self.tel} {self.mail}"

    def get_info(self):
        print(self.firstname)
        print(self.lastname)
        print(self.tel)
        print(self.mail)

    def contact(self):
        print(
            f"Wybieram numer {self.tel} i dzwonię do {self.firstname} {self.lastname}.")

    @property
    def label_length(self):
        return self._label_length


# Wizytówka biznesowa:........................................................................................................
class BusinessContact(BaseContact):
    def __init__(self, firstname, lastname, tel, mail, biztel, job):
        super().__init__(firstname, lastname, tel, mail)
        self.tel = biztel
        self._job = job

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value


# Generator wizytówek:..............................................................................................................
def create_contacts(how_many=1, is_business=False, loud=False):
    '''
    Generates list of contacts.
    First argument determines length of list (how many contacts). Default 1.
    Second if true generates business contact, if false base contact. Default false => base contact.
    Last is to log about inside processes and prints contact. Default false.
    >>> create_contacts()
    >>> create_contacts(3, True, True)
    '''
    contacts_list = []
    for i in range(how_many):
        enpec = random_npc()
        if is_business:
            one_contact = BusinessContact(*enpec)
        else:
            one_contact = BaseContact(*enpec[:-2])
        if loud:
            print("")
            print("Name, LName, PrivPhone, Mail, BusiPhone, Job")
            print(enpec)
            one_contact.contact()
        contacts_list.append(one_contact)
    return contacts_list

    # Wypróbowanie kodu:..........................................................................................................
if __name__ == "__main__":
    base = create_contacts(2, False, True)
    biz = create_contacts(2, True, True)
    '''
    for i in base:
        i.contact()
    print("")
    for i in biz:
        i.contact()
        '''

'''
    enpec = random_npc()
    print(enpec)

    wiz1 = BaseContact(*enpec[:-2])
    print("Base Contact:")
    print(wiz1)
    wiz1.contact()

    wiz2 = BusinessContact(*enpec)
    print("Business Contact:")
    print(wiz2)
    wiz2.contact()

    print(wiz2.job)
    wiz2.job = "Menedżer"
    print(wiz2.job)
'''
