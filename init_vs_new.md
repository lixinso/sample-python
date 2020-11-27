

Use __new__ when you need to control the creation of a new instance.

Use __init__ when you need to control initialization of a new instance.

__new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.

In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.




https://stackoverflow.com/questions/674304/why-is-init-always-called-after-new#:~:text=__new__%20is%20the,instance%20after%20it's%20been%20created.
