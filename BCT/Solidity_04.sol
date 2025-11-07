// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // ✅ Structure
    struct Student {
        string name;
        uint256 age;
    }

    // ✅ Array of Structures
    Student[] public students;

    // ✅ Event when student is added
    event StudentAdded(string name, uint256 age);

    // ✅ Function to add student
    function addStudent(string memory _name, uint256 _age) public {
        students.push(Student(_name, _age));
        emit StudentAdded(_name, _age);
    }

    // ✅ Get student by index
    function getStudent(uint index) public view returns (string memory, uint256) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.name, s.age);
    }

    // ✅ Number of students
    function getCount() public view returns (uint256) {
        return students.length;
    }

    // ✅ Fallback to handle unknown function calls
    fallback() external payable {
        // Accept ether but ignore
    }

    // ✅ Receive Ether
    receive() external payable {}
}
