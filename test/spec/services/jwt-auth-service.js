'use strict';

describe('Service: jwtAuthService', function () {

  // load the service's module
  beforeEach(module('cheeperApp'));

  // instantiate service
  var jwtAuthService;
  beforeEach(inject(function (_jwtAuthService_) {
    jwtAuthService = _jwtAuthService_;
  }));

  it('should do something', function () {
    expect(!!jwtAuthService).toBe(true);
  });

});
