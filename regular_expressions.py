"""
Regular Expressions.

Special Symbols and Characters: The Metacharacters
****************************************************************************
Notation        Description                                   Example Regex
***************************************************************************
 literal         match literal string value literal                 foo
                                                                   arun

 re1|re2         match reg ex. re1 or re2                      foo | bar 
                                                               arun | dev

    .            match any character (except \n)               b.b



Flags available. to use them: (?F)
i - re.I/IGNORECASE
m - re.M/MULTILINE
s - re.S/DOTALL

re_object 
    group()
    start()
    span()
    end()
"""

import re

def print_re(re_exp):
    if re_exp:
        print 'group: ', re_exp.group()
        print 'start: ', re_exp.start()
        print 'span: ', re_exp.span()
        print 'end: ', re_exp.end()
    else:
        print 'None.'
    print '\n\n'
    return True


if __name__ == "__main__":
    str1 = "arun dev"
    res1 = re.match(str1, "arun dev")
    print_re(res1)

    re_c = re.compile('[a-z]+')
    print (re_c)
    str2 = "123456"
    str3 = "superman"
    str4 = "hulk123flash"
    str5 = "a2b2c3d4e5"
   
    print "str2: ", str2
    res2 = re_c.match(str2)
    print_re(res2)


    print "str3: ", str3
    res3 = re_c.match(str3)
    print_re(res3)

    print "str4: ", str4
    res4 = re_c.match(str4)
    print_re(res4)

    print "str5: ", str5
    res5 = re_c.match(str5)
    print_re(res5)

