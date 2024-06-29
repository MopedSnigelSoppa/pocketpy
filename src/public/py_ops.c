#include "pocketpy/interpreter/vm.h"
#include "pocketpy/pocketpy.h"

int py_eq(const py_Ref lhs, const py_Ref rhs) { return 0; }

int py_le(const py_Ref lhs, const py_Ref rhs) { return 0; }

int py_hash(const py_Ref val, int64_t* out) { return 0; }

int py_str(const py_Ref val) { return 0; }

int py_repr(const py_Ref val) {
    const pk_TypeInfo* ti = c11__at(pk_TypeInfo, &pk_current_vm->types, val->type);
    if(ti->m__repr__) return ti->m__repr__(1, val);
    return py_callmethod(val, __repr__);
}

int py_getattr(const py_Ref self, py_Name name, py_Ref out){
    return -1;
}

int py_setattr(py_Ref self, py_Name name, const py_Ref val){
    return -1;
}

int py_callmethod(py_Ref self, py_Name name, ...){
    return -1;
}