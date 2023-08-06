// Class backing the actions ux.

class echolocator__ImageEditUx extends echolocator__UxAutoUpdate {
    COOKIE_NAME = "IMAGE_EDIT_UX";
    FETCH_IMAGE = "echolocator_guis::commands::fetch_image";
    SET_IMAGE_IS_USABLE = "echolocator_guis::commands::set_image_is_usable";

    #jquery_objects = {};
    #autoid = null;
    #record = null;
    #raphael = null;
    #transformer = null;
    #pixel_ux = null;


    constructor(runtime, plugin_link_name, $interaction_parent) {
        super(runtime);

        this.plugin_link_name = plugin_link_name;
        this.$interaction_parent = $interaction_parent;
    }

    // -------------------------------------------------------------
    // Activate things on the UX.

    activate() {
        var F = "echolocator__ImageEditUx::activate"
        super.activate()

        // Make a spreader which reacts to resizing of the window.
        this.image1_spreader = new webviz__Spreader(this);

        // Make a raphael drawing object.
        this.#raphael = Raphael("raphael1_paper", 4000, 4000);

        // For transforming coordinates between data and view.
        this.#transformer = new webviz__Transformer(this.runtime);

        // Pass this transformer to anyone who wants to use the raphael for drawing.
        this.#raphael.webviz_transformer = this.#transformer;

        this.#jquery_objects.$raphael1_paper = $("#raphael1_paper SVG", this.$interaction_parent);
        this.#jquery_objects.$image = $("IMG", this.$interaction_parent);
        this.#jquery_objects.$filename = $(".T_filename", this.$interaction_parent);
        this.#jquery_objects.$number_of_crystals = $(".T_number_of_crystals", this.$interaction_parent);
        this.#jquery_objects.$is_usable = $(".T_is_usable", this.$interaction_parent);
        this.#jquery_objects.previous_button = $(".T_previous_button", this.$interaction_parent);
        this.#jquery_objects.accept_button = $(".T_accept_button", this.$interaction_parent);
        this.#jquery_objects.reject_button = $(".T_reject_button", this.$interaction_parent);
        this.#jquery_objects.reset_button = $(".T_reset_button", this.$interaction_parent);
        this.#jquery_objects.next_button = $(".T_next_button", this.$interaction_parent);

        console.log(F + ": raphael1_paper is a " + this.selector_description(this.#jquery_objects.$raphael1_paper))
        var that = this;

        // Window size changes.
        this.image1_spreader.addEventListener(
            webviz__Spreader__SpreadEvent,
            function (event) { that.handle_spread_event(event); });

        // Set up jquery event handling for DOM elements.
        this.#jquery_objects.$raphael1_paper.click(
            function (jquery_event_object) {
                that._handle_canvas_left_click(jquery_event_object);
            });

        // Disable context menu for right-click on the image.
        this.#jquery_objects.$raphael1_paper.contextmenu(function (jquery_event_object) {
            that._handle_canvas_right_click(jquery_event_object);
            return false;
        });

        this.#jquery_objects.previous_button.click(
            function (jquery_event_object) {
                console.log(F + ": clicked previous");
                that._handle_previous_or_next(-1);
            });

        this.#jquery_objects.accept_button.click(
            function (jquery_event_object) {
                that._handle_is_usable_change(true);
            });

        this.#jquery_objects.reject_button.click(
            function (jquery_event_object) {
                that._handle_is_usable_change(false);
            });

        this.#jquery_objects.reset_button.click(
            function (jquery_event_object) {
                that._handle_is_usable_change(null);
            });

        this.#jquery_objects.next_button.click(
            function (jquery_event_object) {
                that._handle_previous_or_next(1);
            });

        this.#pixel_ux = new echolocator__PixelUx(
            self.runtime,
            "pixel",
            $("#pixel_ux_interaction_parent"));

        // Activate the spreader to react on window size changes.
        this.image1_spreader.activate($("#image1"), window);

        this.#pixel_ux.activate(this.#raphael);

        this.request_update()
    } // end method


    // -------------------------------------------------------------
    // When the selected filename changes, we get notified.
    // We will load the image into the display.

    set_autoid(autoid) {
        var F = "echolocator__ImageEditUx::set_autoid";

        // Remember the image info.
        this.#autoid = autoid;

        if (this.#autoid === undefined) {
            this.display_ajax_error("there are no more images to view");
        }
        else {
            this.display_ajax_error(null);

            // Request image info from the server.
            this.request_update()

        }

    } // end method

    // -------------------------------------------------------------
    // Handle accept or reject button click.

    _handle_is_usable_change(is_usable) {
        var F = "echolocator__ImageEditUx::_handle_is_usable_change";

        if (this.#autoid) {
            // Build json request.
            var json_object = {}
            // TODO: Remove hardcoded "IMAGE_LIST_UX" in image edit's cookie list.
            json_object[this.ENABLE_COOKIES] = [this.COOKIE_NAME, "IMAGE_LIST_UX"]
            json_object[this.COMMAND] = this.SET_IMAGE_IS_USABLE;
            json_object["autoid"] = this.#autoid;
            json_object["is_usable"] = is_usable;

            // Send request to update database immediately.
            this.send(json_object);

            if (!is_usable) {
                // Notify pixel_ux of requested change in position.
                // TODO: Combine usable change with position change into single ajax.
                this.#pixel_ux.set_autoid(this.#autoid, { x: 10, y: 10 });

                // Tell pixel_ux to send change to the database.
                this.#pixel_ux.update_database();
            }

            // Move to next image.
            this.request_update(1);
        }

    } // end method

    // -------------------------------------------------------------
    // Handle previous or next button click.

    _handle_previous_or_next(direction) {
        var F = "echolocator__ImageEditUx::_handle_previous_or_next";

        // Request an update from the database.
        this.request_update(direction);

    } // end method

    // -------------------------------------------------------------
    // Handle left click on the raphael paper.

    _handle_canvas_left_click(jquery_event_object) {
        var F = "echolocator__ImageEditUx::_handle_canvas_left_click";

        var view_position = {
            x: jquery_event_object.offsetX,
            y: jquery_event_object.offsetY
        }

        // Convert to target position before giving to pixel_ux.
        var target_position = this.#transformer.view_to_data(view_position);

        console.log(F + ": clicked view_position" +
            " [" + view_position.x + ", " + view_position.y + "]" +
            " transformed to target_position" +
            " [" + target_position.x + ", " + target_position.y + "]");

        // Notify pixel_ux of requested change in position.
        this.#pixel_ux.set_autoid(this.#autoid, target_position);

        // Tell pixel_ux to send change to the database.
        this.#pixel_ux.update_database();

        // Mark image usable.
        this._handle_is_usable_change(true)

    } // end method

    // -------------------------------------------------------------
    // Handle right click on the raphael paper.

    _handle_canvas_right_click(jquery_event_object) {
        var F = "echolocator__ImageEditUx::_handle_canvas_right_click";

        // Mark image unusable.
        this._handle_is_usable_change(false)

    } // end method
    // -------------------------------------------------------------
    // Request update from database.

    request_update(direction = 0) {

        var json_object = {}
        // TODO: Remove hardcoded "IMAGE_LIST_UX" in image edit's cookie list.
        json_object[this.ENABLE_COOKIES] = [this.COOKIE_NAME, "IMAGE_LIST_UX"]
        json_object[this.COMMAND] = this.FETCH_IMAGE;
        json_object["autoid"] = this.#autoid;
        json_object["direction"] = direction;

        this.send(json_object);

    } // end method

    // -------------------------------------------------------------
    // Handle the response when it comes.

    handle_ajax_success(response, status, jqXHR) {
        var F = "echolocator__ImageEditUx::_handle_ajax_success";

        // Let the base class check for and display any error in the response.
        var error_message = super.handle_ajax_success(response, status, jqXHR);

        if (error_message !== null)
            return;

        // Response is expected to contain the database record.
        var record = response.record;

        if (record === null) {
            console.log(F + ": response record had value of null");
            this.display_ajax_error("Please choose an image.");
            return;
        }

        // Remember which autoid we are showing.
        this.#autoid = record.autoid;

        // Update the display with the new file's contents.
        var src = record.filename;
        this.#jquery_objects.$image.prop("src", src)

        // Render the autoid stuff.
        this.#jquery_objects.$filename.text(record.filename);
        if (record.is_usable === null)
            record.is_usable = "-";
        if (record.is_usable === 1)
            record.is_usable = "yes";
        if (record.is_usable === 0)
            record.is_usable = "no";

        if (record.number_of_crystals === null)
            record.number_of_crystals = "-";

        this.#jquery_objects.$number_of_crystals.text(record.number_of_crystals);
        this.#jquery_objects.$is_usable.text(record.is_usable);

        // Keep the last record loaded.
        this.#record = record;

        // The the pixel ux about the autoid so it can be included in sending changes.
        var target_position = { x: record.target_position_x ? record.target_position_x : 10, y: record.target_position_y ? record.target_position_y : 10 }
        this.#pixel_ux.set_autoid(this.#autoid, target_position);

        // Let the spreader calculate the available space for the image.
        // This will trigger a call to this.handle_spread_event().
        // This only needs to be here for the very first opening of this tab.
        this.image1_spreader.spread();

        // Resize the image to fit on the screen.
        this.resize_image()
    } // end method 

    // -----------------------------------------------------------------------
    // Callback from the spreader event (window resize), after the image size is calculated.
    handle_spread_event(event) {
        var F = "echolocator__ImageEditUx::handle_spread_event";

        // Redraw after window size changed.
        this.render()

    } // end method

    // -----------------------------------------------------------------------
    // Called when window size changes.

    render() {
        var F = "echolocator__ImageEditUx::render";

        var w = $("#image1_viewport").width()
        var h = $("#image1_viewport").height()

        console.log(F + " image1_viewport size is [" + w + ", " + h + "]");

        // Resize the annotation overlay.
        $("#raphael1_viewport").width(w)
        $("#raphael1_viewport").height(h)

        // To transform coordinates.
        this.#transformer.set_view({ x1: 0, y1: 0, x2: w, y2: h })

        // Resize the displayed image according to the current screen size.
        this.resize_image()

        // Tell pixel_ux to render under the new transformer.
        this.#pixel_ux.render()

    } // end method

    // -----------------------------------------------------------------------
    // Resize the displayed image according to the current screen size.

    resize_image() {
        var F = "echolocator__ImageEditUx::resize_image";

        if (this.#record === null)
            return;

        var record = this.#record;

        var w = record.width;
        var h = record.height;

        console.log(F + " image data size is [" + w + ", " + h + "]");

        // To transform coordinates.
        this.#transformer.set_data({ x1: 0, y1: 0, x2: w, y2: h })

        // Transform data to view.
        var view_position = this.#transformer.data_to_view({ x: w, y: h })

        console.log(F + " data to view is [" + view_position.x + ", " + view_position.y + "]");

        // TODO: Move detector1_image resize into image_edit_ux.
        var $img = $("#detector1_image")
        $img.prop("width", view_position.x)
        $img.prop("height", view_position.y)

    } // end method

} // end class