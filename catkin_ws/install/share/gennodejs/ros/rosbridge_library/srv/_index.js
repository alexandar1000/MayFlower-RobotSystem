
"use strict";

let TestRequestAndResponse = require('./TestRequestAndResponse.js')
let AddTwoInts = require('./AddTwoInts.js')
let TestMultipleResponseFields = require('./TestMultipleResponseFields.js')
let TestNestedService = require('./TestNestedService.js')
let TestMultipleRequestFields = require('./TestMultipleRequestFields.js')
let TestResponseOnly = require('./TestResponseOnly.js')
let SendBytes = require('./SendBytes.js')
let TestRequestOnly = require('./TestRequestOnly.js')
let TestArrayRequest = require('./TestArrayRequest.js')
let TestEmpty = require('./TestEmpty.js')

module.exports = {
  TestRequestAndResponse: TestRequestAndResponse,
  AddTwoInts: AddTwoInts,
  TestMultipleResponseFields: TestMultipleResponseFields,
  TestNestedService: TestNestedService,
  TestMultipleRequestFields: TestMultipleRequestFields,
  TestResponseOnly: TestResponseOnly,
  SendBytes: SendBytes,
  TestRequestOnly: TestRequestOnly,
  TestArrayRequest: TestArrayRequest,
  TestEmpty: TestEmpty,
};
