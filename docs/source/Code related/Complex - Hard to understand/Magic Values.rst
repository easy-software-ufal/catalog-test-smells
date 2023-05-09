Magic Values
^^^^^
Definition:

* Magic Values are literals not defined as constant. Numeric literals are called Magic Numbers, string literals are called Magic Strings.


Code Example:

.. code-block:: javascript

  testcase SIP_CC_PR_TR_SE_TI_004 (inout CSeq loc_CSeq_s, CSeq loc_CSeq_ptcs)
    runs on SipComponent system SipInterfaces
  {
      var SipComponent vptc;
      var Response vResponse;
      var float vdelay;
      vDefault := activate(defaultCCPR());
      vptc := SipComponent.create;
      initConfig1(mtc, vptc, system);
      initMTCphase1(loc_CSeq_s);
      setHeadersPtcInvite(loc_CSeq_s);
      vptc.start(ptcWaitCheckInviteCompletedState(loc_CSeq_ptcs));
      initMTCphase2();
      SIPP.send(INVITE Request s2(vRequestUri, vCallId, loc_CSeq_s, vFrom, vTo, vVia)) to sentlabel;
      vCSeq := loc_CSeq_s;
      awaitingFirstAnyFinalResp(vResponse, loc_CSeq_s);
      setHeadersOnReceiptOfResponse(loc_CSeq_s, vResponse);
      // First Repetition
      repeatRespInTime(vResponse, loc_CSeq_s, PXT1 * 1.5);
      // Second Repetition
      vdelay := minValue(2.0 * PXT1, PXT2) * 1.5;
      repeatRespInTime(vResponse, loc_CSeq_s, vdelay);
      // Third repetition
      vdelay := minValue(4.0 * PXT1, PXT2) * 1.1;
      repeatRespInTime(vResponse, loc_CSeq_s, vdelay);
      sendACK(loc_CSeq_s);
      synchroniseCheckDone();
      waitendptc(vptc);
  } // end testcase SIP_CC_PR_TR_SE_TI_004


References:

.. note ::
    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_ :octicon:`graph;1em`

