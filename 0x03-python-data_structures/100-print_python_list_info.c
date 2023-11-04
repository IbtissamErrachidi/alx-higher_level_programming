#include <Python.h>
#include <listobject.h>

void print_python_list_info(PyObject *p) {
    if (PyList_Check(p)) {
        PyListObject *list = (PyListObject *)p;
        Py_ssize_t size = PyList_GET_SIZE(p);

        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", list->allocated);

        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject *element = PyList_GET_ITEM(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        }
    } else {
        PyErr_SetString(PyExc_TypeError, "Object is not a Python list");
    }
}

static PyObject *print_info(PyObject *self, PyObject *args) {
    PyObject *py_list;

    if (!PyArg_ParseTuple(args, "O", &py_list)) {
        return NULL;
    }

    print_python_list_info(py_list);

    Py_RETURN_NONE;
}

static PyMethodDef methods[] = {
    {"print_info", print_info, METH_VARARGS, "Print information about a Python list."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "listinfo",
    "Python List Info Module",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_listinfo(void) {
    return PyModule_Create(&module);
}

