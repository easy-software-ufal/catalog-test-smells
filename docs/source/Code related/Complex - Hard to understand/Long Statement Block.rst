Long Statement Block
^^^^^
Definitions:

* Long statement block in function, test case or altstep. A long function is more difficult to understand than a short one. Although the use of short functions (i.e. methods) is especially important for modern objectoriented languages, short functions have a certain importance for TTCN-3 as well. Long statement blocks in functions, test cases and altsteps should be decomposed into short functions with meaningful names.


Code Example:

.. code-block:: pseudo

  function ptc_CC_PR_MP_RQ_V_030(CSeq lo cCSeq s) runs on SipComponent {
    var Request vINVITERequest;
    var Request vBYERequest;
    var Request vACKRequest;
    charstring vbranch := "";
    initPTC(locCSeq s);
    vDefault := activate(defaultCCPRPTC());
    alt {
      [] SIPP.receive(INVITERequest r1)->
      value vINVITERequest sendt_label {
      TGuard.stop;
      setHeadersOnReceiptOfInvite(vINVITERequest);
      sendPTC200OKInvite();
      setverdict(pass);
      repeat;
      }
      [] SIPP.receive(ACKRequest r1(vCallId))-> value vACKRequest sendt_label {
        vVia := vACKRequest.msgHeader.via;
        if (ispresent(vVia.viaBody[0].viaParams)) {
          var SemicolonParamList tmp_params := vVia.viaBody[0].viaParams;
          if (checkBranchPresent(tmp_params, vbranch)) {
            if (match(v_branch, ValidBranch)) {
              setverdict(pass);
            } else {
              setverdict(fail);
            };
          } else {
            setverdict(fail)
          };
        } else {
          setverdict(fail)
        };
        cpA.send(CMCheckDone);
        repeat;
      }
      [] SIPP.receive(BYERequest r1(vCallId))-> value vBYERequest sendt_label {
        setHeadersOnReceiptO fBye(vBYERequest);
        send200OK();
      }
      [] cpA.receive(CMStop) {
        all timer.stop;
        stop;
      }
      [] SIPP.receive {
        repeat;
      }
      [] TGuard.timeout {
        setverdict(fail);
        stop;
      }
    }
  }

References:

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_

