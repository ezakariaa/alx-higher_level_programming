#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - print a maximum of 10 bytes
*
* @p: Python Object
* Return: no return
*/
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, max;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	if (size >= 10)
		max = 10;
	else
		max = size + 1;
	printf("  first %ld bytes:", max);
	for (i = 0; i < max; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);
	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *objct;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf(" [*] Python list info\n");
	printf(" [*] Size of the Python List = %ld\n", size);
	printf(" [*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		objct = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((objct)->ob_type)->tp_name);
		if (PyBytes_Check(objct))
			print_python_bytes(objct);
	}
}
