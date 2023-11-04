#include <Python.h>

static PyObject *print_info(PyObject *self, PyObject *args) {
    PyObject *py_list;

    if (!PyArg_ParseTuple(args, "O", &py_list)) {
        return NULL;
    }

    if (PyList_Check(py_list)) {
        PyListObject *list = (PyListObject *)py_list;
        Py_ssize_t size = PyList_Size(py_list);

        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", list->allocated);

        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject *element = PyList_GetItem(py_list, i);
            printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        }
    } else {
        PyErr_SetString(PyExc_TypeError, "Object is not a Python list");
        return NULL;
    }

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

