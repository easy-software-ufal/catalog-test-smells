Bad Comment Rate
^^^^^
Definition:

* The comment rate (number of comments per line) is too high or too low.


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
.. note ::

    Every icon means something:
    - :octicon:`file-code;1em` - Reference has Code Example
    - :octicon:`comment-discussion;1em` - Reference has Cause and Effect
    - :octicon:`graph;1em` - Reference has Frequency

 * `Pattern-based Smell Detection in TTCN-3 Test Suites <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.144.6997&rep=rep1&type=pdf>`_ :octicon:`file-code;1em` :octicon:`comment-discussion;1em`
 * `An approach to quality engineering of TTCN-3 test specifications <https://link.springer.com/article/10.1007/s10009-008-0075-0>`_
 * `Utilising Code Smells to Detect Quality Problems in TTCN-3 Test Suites <https://link.springer.com/chapter/10.1007/978-3-540-73066-8_16>`_

