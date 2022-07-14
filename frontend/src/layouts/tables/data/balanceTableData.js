/* eslint-disable react/prop-types */
/* eslint-disable react/function-component-definition */
/**
=========================================================
* Material Dashboard 2 React - v2.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2022 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

import React, { useEffect, useState } from "react";
import axios from "axios";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDBadge from "components/MDBadge";

export default function data() {
  const [loadingData, setLoadingData] = useState(true);
  const [statuses, setStatuses] = useState([]);

  useEffect(() => {
    async function getData() {
      await axios.get("http://localhost:5000/balance/all").then((res) => {
        setStatuses(res.data.balances);
        setLoadingData(false);
      });
    }
    if (loadingData) {
      getData();
    }
  }, []);

  return {
    columns: [
      { Header: "Account", accessor: "account", align: "left", sortType: "caseInsensitive" },
      { Header: "Currency", accessor: "currency", align: "left", sortType: "caseInsensitive" },
      { Header: "Date", accessor: "date", align: "left", sortType: "caseInsensitive" },
      { Header: "Open", accessor: "open", align: "left", sortType: "caseInsensitive" },
      { Header: "Close", accessor: "close", align: "left", sortType: "caseInsensitive" },
      { Header: "Difference", accessor: "difference", align: "left", sortType: "caseInsensitive" },
      { Header: "Outstanding", accessor: "outstanding", align: "left", sortType: "caseInsensitive" },
      { Header: "Reconciled", accessor: "reconciled", align: "center" },
    ],
    rows: statuses.map((item) => ({
      account: item.account,
      date: item.date,
      currency: item.currency,
      open: item.open,
      close: item.close,
      difference: item.difference,
      outstanding: item.outstanding,
      reconciled: (
        <MDBox ml={-1}>
          <MDBadge
            badgeContent={item.reconciled.toString()}
            color={item.reconciled ? "success" : "error"}
            variant="gradient"
            size="sm"
          />
        </MDBox>
      ),
    })),
  };
}
