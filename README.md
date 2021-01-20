# Pytest_UI

pytest To run all tests

pytest --collect-only finding all possible test

pytest -vs test_vinod.py to specific module

pytest -vs test_vinod.py::test_case_01 to run specific method under module

pytest -vs test_vinod.py::TestVinod::test_case_01 to run specific method under class inside module

-v verbose (to get more information)

-k parameterised run (particular test run)

-m mark case what you want run (smoke / sanity / regression)

-s to get print output (print("something from testcases"))

-n number of loop (n 3)

--------------------------------------------------------------------------------------------
pytest -m "not event" (to skip "event" mark testcases)

pytest -m "event or smoke" -v (or condition applied on markers)

pytest -m "event and smoke" -v (and condition applied on markers)

--------------------------------------------------------------------------------------------
class mark - All above will work along with this 
             (have to mark at global level i.e., mark above the class)

--------------------------------------------------------------------------------------------
fixture - Fixtures are functions, which will run before each test function 
          to which it is applied. Fixtures are used to feed some data to the
          tests such as database connections, URLs to test, and some sort of input data

--------------------------------------------------------------------------------------------
Scope - will use in FIXTURES. And also scope have (Module / Class / Function / Session)

Function = it launches the browser 2 times for each function or method call
Class    = it launches the browser 2 times for each function or method call
Module   = it maintains same browser launch to run the different function or method call
Session  = it maintains same browser launch to run the different function or method call

------------------------------------------------------------------------------------------
Parametrization can do at "mark level" and "fixture level" 

@mark.Parametrize("vinod,sreevani"[("B.tech","Tirupati"),("B.tech","nellore")]) 
ex::- 
def parents(name1, name2)
print("I am {name1} and {name2}")

@fixture.Parametrize(params=["vinod","sreevani"])
ex::- 
@fixture(params=['https://www.flipkart.com/', 'https://www.amazon.in/'])
def values(request):
    return request.param

@mark.event
def chrome_crpo(setup, values):
    print('launch browser')
    setup.get(values)
    time.sleep(3)
    var = setup.title
    print(var)

---------------------------------------------------------------------------------------------- 
Config files (Config.ini) allows us to provide configurations 
1. app configurations
2. sensitive information
3. a different config for different environment

---------------------------------- configparser -----------------------------------------------