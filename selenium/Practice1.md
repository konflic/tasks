# Selenium practice 1

Use https://demo.opencart.com for practice.

1. Create new github project with basic setup (README.md, .gitignore)
2. In new branch ```basic_setup``` create the following: 
  - In conftest.py create browser fixture with finalizer. 
  - Make options for pytest```--browser``` and ```--url``` to control opening provided url and browser.
3. Merge this changes into main/master branch.
  - In new branch ```first_tests``` write tests for opencart application: 
  - Test that checks availability of all links on top-bar in opencart.
  - Test that checks availability of currency button in top panel.
  - Test that checks availability of all elements on admin login panel.
  - Test that checks serach input and cart button on main page.
4. Merge this branch into your main/master branch.
