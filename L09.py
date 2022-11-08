import requests
import pytest
def main():
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
    response = requests.get("https://api.duckduckgo.com/?q='presidents of the united states,'&format=json")
    response = response.json()
    #print(response['RelatedTopics'])
    nameList = []
    for item in response['RelatedTopics']:
        strItem = item['Result']
        slicingIndex = (strItem.find(">") + 1)
        strItem = strItem[slicingIndex:]
        slicingIndex = (strItem.find("<"))
        nameList.append(strItem[0:slicingIndex])
    global nameSet
    nameSet = set(nameList)
    print(nameSet)


def test_1():
    main()
    bln = False
    if "George Washington" in nameSet:
        bln = True
    assert bln == True

def test_2():
    main()
    bln = False
    if "John Adams" in nameSet:
        bln = True
    assert bln == True

def test_3():
    main()
    bln = False
    if "Thomas Jefferson" in nameSet:
        bln = True
    assert bln == True

def test_4():
    main()
    bln = False
    if "James Madison" in nameSet:
        bln = True
    assert bln == True

def test_5():
    main()
    bln = False
    if "James Monroe" in nameSet:
        bln = True
    assert bln == True

def test_6():
    main()
    bln = False
    if "John Quincy Adams" in nameSet:
        bln = True
    assert bln == True

def test_7():
    main()
    bln = False
    if "Andrew Jackson" in nameSet:
        bln = True
    assert bln == True

def test_8():
    main()
    bln = False
    if "Martin Van Buren" in nameSet:
        bln = True
    assert bln == True

def test_9():
    main()
    bln = False
    if "William Henry Harrison" in nameSet:
        bln = True
    assert bln == True

def test_10():
    main()
    bln = False
    if "John Tyler" in nameSet:
        bln = True
    assert bln == True

def test_11():
    main()
    bln = False
    if "James K. Polk" in nameSet:
        bln = True
    assert bln == True

def test_12():
    main()
    bln = False
    if "Zachary Taylor" in nameSet:
        bln = True
    assert bln == True

def test_13():
    main()
    bln = False
    if "Millard Fillmore" in nameSet:
        bln = True
    assert bln == True

def test_14():
    main()
    bln = False
    if "Franklin Pierce" in nameSet:
        bln = True
    assert bln == True

def test_15():
    main()
    bln = False
    if "James Buchanan" in nameSet:
        bln = True
    assert bln == True

def test_16():
    main()
    bln = False
    if "Abraham Lincoln" in nameSet:
        bln = True
    assert bln == True

def test_17():
    main()
    bln = False
    if "Andrew Johnson" in nameSet:
        bln = True
    assert bln == True

def test_18():
    main()
    bln = False
    if "Ulysses S. Grant" in nameSet:
        bln = True
    assert bln == True

def test_19():
    main()
    bln = False
    if "Rutherford B. Hayes" in nameSet:
        bln = True
    assert bln == True

def test_20():
    main()
    bln = False
    if "James Garfield" in nameSet:
        bln = True
    assert bln == True

def test_21():
    main()
    bln = False
    if "Chester A. Arthur" in nameSet:
        bln = True
    assert bln == True

def test_22():
    main()
    bln = False
    if "Grover Cleveland" in nameSet:
        bln = True
    assert bln == True

def test_23():
    main()
    bln = False
    if "Benjamin Harrison" in nameSet:
        bln = True
    assert bln == True

def test_24():
    main()
    bln = False
    if "William McKinley" in nameSet:
        bln = True
    assert bln == True

def test_25():
    main()
    bln = False
    if "Theodore Roosevelt" in nameSet:
        bln = True
    assert bln == True

def test_26():
    main()
    bln = False
    if "William Howard Taft" in nameSet:
        bln = True
    assert bln == True

def test_27():
    main()
    bln = False
    if "Woodrow Wilson" in nameSet:
        bln = True
    assert bln == True

def test_28():
    main()
    bln = False
    if "Warren G. Harding" in nameSet:
        bln = True
    assert bln == True

def test_29():
    main()
    bln = False
    if "Calvin Coolidge" in nameSet:
        bln = True
    assert bln == True

def test_30():
    main()
    bln = False
    if "Herbert Hoover" in nameSet:
        bln = True
    assert bln == True

def test_31():
    main()
    bln = False
    if "Franklin D. Roosevelt" in nameSet:
        bln = True
    assert bln == True

def test_32():
    main()
    bln = False
    if "Harry S. Truman" in nameSet:
        bln = True
    assert bln == True

def test_33():
    main()
    bln = False
    if "Dwight D. Eisenhower" in nameSet:
        bln = True
    assert bln == True

def test_34():
    main()
    bln = False
    if "John F. Kennedy" in nameSet:
        bln = True
    assert bln == True

def test_35():
    main()
    bln = False
    if "Lyndon B. Johnson" in nameSet:
        bln = True
    assert bln == True

def test_36():
    main()
    bln = False
    if "Richard M. Nixon" in nameSet:
        bln = True
    assert bln == True

def test_37():
    main()
    bln = False
    if "Gerald R. Ford" in nameSet:
        bln = True
    assert bln == True

def test_38():
    main()
    bln = False
    if "James Carter" in nameSet:
        bln = True
    assert bln == True

def test_39():
    main()
    bln = False
    if "Ronald Reagan" in nameSet:
        bln = True
    assert bln == True

def test_40():
    main()
    bln = False
    if "George H. W. Bush" in nameSet:
        bln = True
    assert bln == True

def test_41():
    main()
    bln = False
    if "William J. Clinton" in nameSet:
        bln = True
    assert bln == True

def test_42():
    main()
    bln = False
    if "George W. Bush" in nameSet:
        bln = True
    assert bln == True

def test_43():
    main()
    bln = False
    if "Barack Obama" in nameSet:
        bln = True
    assert bln == True

def test_44():
    main()
    bln = False
    if "Donald Trump" in nameSet:
        bln = True
    assert bln == True

def test_45():
    main()
    bln = False
    if "Joseph R. Biden Jr." in nameSet:
        bln = True
    assert bln == True




