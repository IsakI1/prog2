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

<<<<<<< HEAD
double Person::getDecades(){
	return static_cast<double>(age) / 10.0;
=======
int Person::getDecades(){
	return double(age/10.0);
>>>>>>> 703f420fe1c9965d17af69c72175da6ecf04f9b5
	}


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
