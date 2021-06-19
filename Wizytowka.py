from faker import Faker
import random
fak = Faker()


# Tutaj stworzyłem funkcje, które generują fałszywe dane osobowe:.......................................................
# faketel lepiej wygląda w ten sposób, niż korzystając z fakera moim zdaniem.
def faketel():
    tel = "+48"
    for i in range(3):
        tel += " " + f"000{random.randint(0,999)}"[-3:]
    return tel


def fakemail(firstname, lastname):
    maildomains = ["gmail", "onet", "interia"]
    mailextentions = [".com", ".pl", ".com.pl"]
    privmail = f"{firstname}.{lastname}@{random.choice(maildomains)}{random.choice(mailextentions)}"

    mail_domain = fak.domain_name()
    bizmail = f"{firstname}.{lastname}@{mail_domain}"
    return privmail, bizmail


def random_npc():
    firstname = fak.first_name()
    lastname = fak.last_name()
    privtel = faketel()
    biztel = faketel()
    privmail, bizmail = fakemail(firstname, lastname)
    return [firstname, lastname, privtel, privmail, biztel, bizmail]


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

    @label_length.setter
    def label_length(self, value):
        self._label_length = value


# Wizytówka biznesowa:........................................................................................................
class BusinessContact(BaseContact):
    def __init__(self, firstname, lastname, tel, mail, biztel, bizmail):
        super().__init__(firstname, lastname, tel, mail)
        self.tel = biztel
        self.mail = bizmail


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
            print("Name, LName, PrivPhone, PrivMail, BusiPhone, BusiMail")
            print(enpec)
            one_contact.contact()
        contacts_list.append(one_contact)
    return contacts_list

    # Wypróbowanie kodu:..........................................................................................................
if __name__ == "__main__":
    base = create_contacts(2, False)
    biz = create_contacts(2, True)
    for i in base:
        i.contact()
    print("")
    for i in biz:
        i.contact()
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


    print(wiz1.label_length)
    wiz1.label_length = 10
    print(wiz1.label_length)
    '''
