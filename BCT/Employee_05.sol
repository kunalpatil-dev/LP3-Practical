// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract EmployeeDetails {

    struct Employee {
        uint256 empId;
        string name;
        uint256 salary;
        string joiningDate;
    }

    Employee public emp;

    // Set / update employee details
    function setEmployee(
        uint256 _empId,
        string memory _name,
        uint256 _salary,
        string memory _joiningDate
    ) public {
        emp = Employee(_empId, _name, _salary, _joiningDate);
    }

    // Get employee details
    function getEmployee() public view returns (
        uint256,
        string memory,
        uint256,
        string memory
    ) {
        return (emp.empId, emp.name, emp.salary, emp.joiningDate);
    }
}
