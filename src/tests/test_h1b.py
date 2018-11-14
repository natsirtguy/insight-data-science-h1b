'''Test h1b_counting.py.'''
import pytest
from collections import Counter
from context import h1b_counting


@pytest.fixture
def visas():
    '''A fixture to simulate an input file.'''
    lines = ''';CASE_NUMBER;CASE_STATUS;CASE_SUBMITTED;DECISION_DATE;VISA_CLASS;EMPLOYMENT_START_DATE;EMPLOYMENT_END_DATE;EMPLOYER_NAME;EMPLOYER_BUSINESS_DBA;EMPLOYER_ADDRESS;EMPLOYER_CITY;EMPLOYER_STATE;EMPLOYER_POSTAL_CODE;EMPLOYER_COUNTRY;EMPLOYER_PROVINCE;EMPLOYER_PHONE;EMPLOYER_PHONE_EXT;AGENT_REPRESENTING_EMPLOYER;AGENT_ATTORNEY_NAME;AGENT_ATTORNEY_CITY;AGENT_ATTORNEY_STATE;JOB_TITLE;SOC_CODE;SOC_NAME;NAICS_CODE;TOTAL_WORKERS;NEW_EMPLOYMENT;CONTINUED_EMPLOYMENT;CHANGE_PREVIOUS_EMPLOYMENT;NEW_CONCURRENT_EMP;CHANGE_EMPLOYER;AMENDED_PETITION;FULL_TIME_POSITION;PREVAILING_WAGE;PW_UNIT_OF_PAY;PW_WAGE_LEVEL;PW_SOURCE;PW_SOURCE_YEAR;PW_SOURCE_OTHER;WAGE_RATE_OF_PAY_FROM;WAGE_RATE_OF_PAY_TO;WAGE_UNIT_OF_PAY;H1B_DEPENDENT;WILLFUL_VIOLATOR;SUPPORT_H1B;LABOR_CON_AGREE;PUBLIC_DISCLOSURE_LOCATION;WORKSITE_CITY;WORKSITE_COUNTY;WORKSITE_STATE;WORKSITE_POSTAL_CODE;ORIGINAL_CERT_DATE
0;I-200-18026-338377;CERTIFIED;2018-01-29;2018-02-02;H-1B;2018-07-28;2021-07-27;MICROSOFT CORPORATION;;1 MICROSOFT WAY;REDMOND;WA;98052;UNITED STATES OF AMERICA;;4258828080;;N;",";;;SOFTWARE ENGINEER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";51121.0;1;0;1;0;0;0;0;Y;112549.0;Year;Level II;OES;2017.0;OFLC ONLINE DATA CENTER;143915.0;0.0;Year;N;N;;;;REDMOND;KING;WA;98052;
1;I-200-17296-353451;CERTIFIED;2017-10-23;2017-10-27;H-1B;2017-11-06;2020-11-06;ERNST & YOUNG U.S. LLP;;200 PLAZA DRIVE;SECAUCUS;NJ;07094;UNITED STATES OF AMERICA;;2018723003;;Y;"BRADSHAW, MELANIE";TORONTO;;TAX SENIOR;13-2011;ACCOUNTANTS AND AUDITORS;541211.0;1;0;0;0;0;1;0;Y;79976.0;Year;Level II;OES;2017.0;OFLC ONLINE DATA CENTER;100000.0;0.0;Year;N;N;;;;SANTA CLARA;SAN JOSE;CA;95110;
2;I-200-18242-524477;CERTIFIED;2018-08-30;2018-09-06;H-1B;2018-09-10;2021-09-09;LOGIXHUB LLC;;320 DECKER DRIVE;IRVING;TX;75062;UNITED STATES OF AMERICA;;2145419305;;N;",";;;DATABASE ADMINISTRATOR;15-1141;DATABASE ADMINISTRATORS;541511.0;1;0;0;0;0;1;0;Y;77792.0;Year;Level II;OES;2018.0;OFLC ONLINE DATA CENTER;78240.0;0.0;Year;N;N;;;;IRVING;DALLAS;TX;75062;
3;I-200-18070-575236;CERTIFIED;;2018-03-30;H-1B;2018-09-10;2021-09-09;"HEXAWARE TECHNOLOGIES, INC.";;101 WOOD AVENUE SOUTH;ISELIN;NJ;08830;UNITED STATES OF AMERICA;;6094096950;;Y;"DUTOT, CHRISTOPHER";TROY;MI;SOFTWARE ENGINEER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;5;5;0;0;0;0;0;Y;84406.0;Year;Level II;OES;2017.0;OFLC ONLINE DATA CENTER;84406.0;85000.0;Year;Y;N;Y;;;NEW CASTLE;NEW CASTLE;DE;19720;
4;I-200-18243-850522;CERTIFIED;2018-08-31;2018-09-07;H-1B;2018-09-07;2021-09-06;"ECLOUD LABS,INC.";;120 S WOOD AVENUE;ISELIN;NJ;08830;UNITED STATES OF AMERICA;;7327501323;;Y;"ALLEN, THOMAS";EDISON;NJ;MICROSOFT DYNAMICS CRM APPLICATION DEVELOPER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;0;0;0;0;1;Y;87714.0;Year;Level III;OES;2018.0;OFLC ONLINE DATA CENTER;95000.0;0.0;Year;Y;N;Y;Y;;BIRMINGHAM;SHELBY;AL;35244;
5;I-200-18142-939501;CERTIFIED;2018-05-22;2018-05-29;H-1B;2018-05-29;2021-05-28;OBERON IT;;1404 W WALNUT HILL LN;IRVING;TX;75038;UNITED STATES OF AMERICA;;8666609190;;Y;"GARRITSON, JAMES";RICHARDSON;TX;SENIOR SYSTEM ARCHITECT;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;0;0;0;0;1;Y;71864.0;Year;Level II;Other;2017.0;OFLC ONLINE DATA CENTER;74000.0;0.0;Year;Y;N;Y;;;SUNRISE;BROWARD;FL;33323;
6;I-200-18121-552858;CERTIFIED;2018-05-01;2018-05-07;H-1B;2018-05-02;2018-10-26;ICONSOFT INC.;;101 CAMBRIDGE STREET SUITE 360;BURLINGTON;MA;01803;UNITED STATES OF AMERICA;;8882054614;1;N;",";;;SENIOR ORACLE ADF DEVELOPER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;1;0;0;0;0;Y;92331.0;Year;Level III;Other;2017.0;OFLC ONLINE DATA CENTER;114000.0;0.0;Year;Y;N;Y;;;JACKSONVILLE;DUVAL COUNTY;FL;32202;
7;I-200-18215-849606;CERTIFIED;2018-08-03;2018-08-09;H-1B;2018-08-11;2021-08-11;COGNIZANT TECHNOLOGY SOLUTIONS US CORP;;211 QUALITY CIRCLE;COLLEGE STATION;TX;77845;UNITED STATES OF AMERICA;;2019661249;;N;",";;;SENIOR SYSTEMS ANALYST JC60;15-1121;COMPUTER SYSTEMS ANALYST;541512.0;1;0;1;0;0;0;0;Y;80579.0;Year;Level II;OES;2018.0;OFLC ONLINE DATA CENTER;80579.0;0.0;Year;Y;N;Y;;;OWINGS MILLS;BALTIMORE;MD;21117;
8;I-201-17339-472823;CERTIFIED;2017-12-08;2017-12-14;H-1B1 Chile;2017-12-08;2019-06-07;ISHI SYSTEMS INC;;185 HUDSON STREET;JERSEY CITY;NJ;07311;UNITED STATES OF AMERICA;;2013326900;;N;",";;;ASSOCIATE PRODUCT MANAGER(15-1199.09);15-1199;"COMPUTER OCCUPATIONS, ALL OTHER";541511.0;1;0;1;0;0;0;0;Y;88317.0;Year;Level III;OES;2017.0;OFLC ONLINE DATA CENTER;90000.0;0.0;Year;;;;;;JERSEY CITY;HUDSON;NJ;07311;
9;I-200-18233-239931;CERTIFIED;2018-08-21;2018-08-27;H-1B;2018-09-05;2021-09-04;"WB SOLUTIONS, LLC";;7320 E FLETCHER AVE;TAMPA;FL;33637;UNITED STATES OF AMERICA;;8133300099;;Y;"KIDAMBI, VAMAN";TRUMBULL;CT;SENIOR JAVA DEVELOPER;15-1132;"SOFTWARE DEVELOPERS, APPLICATIONS";541511.0;1;0;0;0;0;1;0;Y;104790.0;Year;Level III;OES;2018.0;OFLC ONLINE DATA CENTER;105000.0;0.0;Year;Y;N;Y;Y;;ALPHARETTA;FULTON;GA;30005;
'''.split('\n')
    return iter(lines)


@pytest.fixture
def visa_fields():
    '''The fields from the visa example.'''
    return ''';CASE_NUMBER;CASE_STATUS;CASE_SUBMITTED;DECISION_DATE;VISA_CLASS;EMPLOYMENT_START_DATE;EMPLOYMENT_END_DATE;EMPLOYER_NAME;EMPLOYER_BUSINESS_DBA;EMPLOYER_ADDRESS;EMPLOYER_CITY;EMPLOYER_STATE;EMPLOYER_POSTAL_CODE;EMPLOYER_COUNTRY;EMPLOYER_PROVINCE;EMPLOYER_PHONE;EMPLOYER_PHONE_EXT;AGENT_REPRESENTING_EMPLOYER;AGENT_ATTORNEY_NAME;AGENT_ATTORNEY_CITY;AGENT_ATTORNEY_STATE;JOB_TITLE;SOC_CODE;SOC_NAME;NAICS_CODE;TOTAL_WORKERS;NEW_EMPLOYMENT;CONTINUED_EMPLOYMENT;CHANGE_PREVIOUS_EMPLOYMENT;NEW_CONCURRENT_EMP;CHANGE_EMPLOYER;AMENDED_PETITION;FULL_TIME_POSITION;PREVAILING_WAGE;PW_UNIT_OF_PAY;PW_WAGE_LEVEL;PW_SOURCE;PW_SOURCE_YEAR;PW_SOURCE_OTHER;WAGE_RATE_OF_PAY_FROM;WAGE_RATE_OF_PAY_TO;WAGE_UNIT_OF_PAY;H1B_DEPENDENT;WILLFUL_VIOLATOR;SUPPORT_H1B;LABOR_CON_AGREE;PUBLIC_DISCLOSURE_LOCATION;WORKSITE_CITY;WORKSITE_COUNTY;WORKSITE_STATE;WORKSITE_POSTAL_CODE;ORIGINAL_CERT_DATE'''.split(';')


@pytest.fixture
def top_10_occupations():
    '''The output for the top 10 occupations.'''
    return '''TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
SOFTWARE DEVELOPERS, APPLICATIONS;6;60.0%
ACCOUNTANTS AND AUDITORS;1;10.0%
COMPUTER OCCUPATIONS, ALL OTHER;1;10.0%
COMPUTER SYSTEMS ANALYST;1;10.0%
DATABASE ADMINISTRATORS;1;10.0%
'''


@pytest.fixture
def top_10_states():
    '''The output for the top 10 states.'''
    return '''TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
FL;2;20.0%
AL;1;10.0%
CA;1;10.0%
DE;1;10.0%
GA;1;10.0%
MD;1;10.0%
NJ;1;10.0%
TX;1;10.0%
WA;1;10.0%
'''


@pytest.fixture
def some_counters():
    '''A dictionary of counters for testing produce_top_10s.'''
    counters = {'animals': Counter(['dog', 'dog', 'cat', 'mouse']),
                'ants': Counter()}
    top_10s = {'ANIMALS':
               '''TOP_ANIMALS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
dog;2;50.0%
cat;1;25.0%
mouse;1;25.0%
''',
               'INSECTS':
               '''TOP_INSECTS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE

'''}
    return counters, top_10s


def test_read_visas(visas, top_10_occupations, top_10_states):
    '''Test the read_visas function from h1b_counting.'''
    top10s = h1b_counting.read_visas(
        visas, {'SOC_NAME': 'OCCUPATIONS',
                'WORKSITE_STATE': 'STATES'})
    assert top10s['OCCUPATIONS'] == top_10_occupations
    assert top10s['STATES'] == top_10_states


def test_produce_top_10s(some_counters):
    '''Test produce_top_10s from h1b_counting.'''
    counters, top_10s = some_counters
    assert top_10s == h1b_counting.produce_top_10s(
        counters, {'animals': 'animals', 'ants': 'insects'})