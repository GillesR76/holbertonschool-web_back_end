/**
 * @file 0-get_list_students.js
 * @author TheWatcher01
 * @date 21-05-2024
 * @description This module exports a function that returns a list of students.
 */

/**
 * @function getListStudents
 * @description Function to get the list of students.
 * Each student is an object with `id`, `firstName`, and `location` properties.
 * @returns {Array} Array of student objects.
 */
export default function getListStudents() {
  return [
    // Student object with id 1, firstName 'Guillaume', and location 'San Francisco'
    { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    // Student object with id 2, firstName 'James', and location 'Columbia'
    { id: 2, firstName: 'James', location: 'Columbia' },
    // Student object with id 5, firstName 'Serena', and location 'San Francisco'
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  ];
}
