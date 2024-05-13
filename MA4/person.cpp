#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		double getDecades();
	private:
		int age;
	};
Person::Person(int a){
	age = a;
	}
int Person::getAge(){
	return age;
	}

void Person::setAge(int a){
	age = a;
	}

double Person::getDecades(){
<<<<<<< HEAD
	return double(age)/10.0;
	}
=======
	return age/10.0;
}
int fibonacci(int age) {
    if (age <= 1)
        return age;
    else
        return fibonacci(age-1) + fibonacci(age-2);
}


>>>>>>> f2a279b5a50bd839bc49f2ca93cb9bb5cf1010d2
extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	double Person_getDecades(Person* person) {return person->getDecades();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
