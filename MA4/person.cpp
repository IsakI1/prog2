#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		double getDecades();
		int fib_cpp();
		int fib_cpp_helper(int);
	private:
		int age;
		int n;
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
	return double(age)/10.0;
	}

int Person::fib_cpp() {
	n = getAge();
	return fib_cpp_helper(n);
}

int Person::fib_cpp_helper(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fib_cpp_helper(n-1) + fib_cpp_helper(n-2);
    }
}

	
extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	int Person_fib_cpp(Person* person) { return person->fib_cpp(); }
	double Person_getDecades(Person* person) {return person->getDecades();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
