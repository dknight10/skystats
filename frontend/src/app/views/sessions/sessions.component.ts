import { Component, OnInit } from '@angular/core';

import { SelectionModel } from '@angular/cdk/collections';
import { MatTableDataSource } from '@angular/material/table';

import { SessionsService } from './sessions.service';
import { Session } from './session';

import { rowAnimation, tableAnimation } from './table.animation';

@Component({
  selector: 'skystats-sessions',
  templateUrl: './sessions.component.html',
  styleUrls: ['./sessions.component.scss'],
  animations: [rowAnimation, tableAnimation]
})
export class SessionsComponent implements OnInit {
  dataSource = new MatTableDataSource<Session>();
  selection = new SelectionModel<Session>(true, []);
  displayedColumns = ["select", "timestamp", "name", "type", "shots", "clubs"];
  dataLength: number;

  constructor(private service: SessionsService) { }

  isAllSelected() {
    const numSelected = this.selection.selected.length;
    const numRows = this.dataSource.data.length;
    return numSelected === numRows;
  }

  masterToggle() {
    this.isAllSelected() ?
      this.selection.clear() :
      this.dataSource.data.forEach(row => this.selection.select(row));
  }

  ngOnInit() {
    this.service.getSessions().subscribe(data => {
      this.dataSource.data = data
      this.dataLength = data.length
      this.masterToggle();  // select all rows initially
    });
  }

  noneSelected() {
    return this.selection.selected.length === 0;
  }

  download() {
    if (this.noneSelected()) {
      return;
    }
    let ids = this.selection.selected.map(row => row.id);
    let format = 'excel';
    this.service.download(ids, format).subscribe();
  }
}
