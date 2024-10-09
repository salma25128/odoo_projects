/** @odoo-module **/
import { registry } from '@web/core/registry';
import { useState } from "@odoo/owl";
import { ListController } from "@web/views/list/list_controller";

class TaskHierarchyController extends ListController {
    setup() {
        super.setup();
        this.state = useState({
            sortBy: 'parent_id',
            ascending: true,
        });

        // Validate model existence
        if (!this.props.model) {
            throw new Error('Invalid model name: undefined');
        }
    }

    // Function to toggle sorting
    toggleSort(field) {
        if (this.state.sortBy === field) {
            this.state.ascending = !this.state.ascending;
        } else {
            this.state.sortBy = field;
            this.state.ascending = true;
        }

        this.trigger('field_order', {
            orderBy: [{
                name: this.state.sortBy,
                asc: this.state.ascending,
            }],
        });
    }

    // Render the header with clickable columns for sorting
    _renderHeader() {
        const header = super._renderHeader();

        const nameHeader = header.querySelector('[data-name="name"]');
        const deadlineHeader = header.querySelector('[data-name="date_deadline"]');
        const priorityHeader = header.querySelector('[data-name="priority"]');
        const sequenceHeader = header.querySelector('[data-name="sequence"]');

        if (nameHeader) {
            nameHeader.onclick = () => this.toggleSort('name');
        }
        if (deadlineHeader) {
            deadlineHeader.onclick = () => this.toggleSort('date_deadline');
        }
        if (priorityHeader) {
            priorityHeader.onclick = () => this.toggleSort('priority');
        }
        if (sequenceHeader) {
            sequenceHeader.onclick = () => this.toggleSort('sequence');
        }

        return header;
    }
}

// Register the custom controller
registry.category("controllers").add("task_hierarchy_controller", TaskHierarchyController);
