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

// @mui material components
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

// Material Dashboard 2 React example components
import DataTable from "examples/Tables/DataTable";

// Data
import transactionTableData from "layouts/tables/data/transactionTableData";
import balanceTableData from "layouts/tables/data/balanceTableData";

function Tables() {
  const { columns: transactionColumns, rows: transactionRows } = transactionTableData();
  const { columns: balanceColumns, rows: balanceRows } = balanceTableData();


  return (
    <MDBox pt={6} pb={3}>
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Card>
            <MDBox
              mx={2}
              mt={-4}
              py={1}
              px={2}
              variant="gradient"
              bgColor="info"
              borderRadius="lg"
              coloredShadow="info"
            >
              <MDTypography variant="h6" color="white">
                Balance Status
              </MDTypography>
            </MDBox>
            <MDBox pt={1}>
              <DataTable
                table={{ columns: balanceColumns, rows: balanceRows }}
                isSorted
                entriesPerPage={{ defaultValue: 5 }}
                showTotalEntries={false}
                noEndBorder
              />
            </MDBox>
          </Card>
          <MDBox mx={1}></MDBox>
          <Card>
            <MDBox
              mx={2}
              mt={1}
              py={0.5}
              px={2}
              variant="gradient"
              bgColor="info"
              borderRadius="lg"
              coloredShadow="info"
            >
              <MDTypography variant="h6" color="white">
                Transaction Status
              </MDTypography>
            </MDBox>
            <MDBox pt={1}>
              <DataTable
                table={{ columns: transactionColumns, rows: transactionRows }}
                isSorted
                entriesPerPage={{ defaultValue: 25 }}
                showTotalEntries={false}
              />
            </MDBox>
          </Card>
        </Grid>
      </Grid>
    </MDBox>
    
  );
}

export default Tables;
