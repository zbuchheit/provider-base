// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Component extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'base:index:Component';

    /**
     * Returns true if the given object is an instance of Component.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Component {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Component.__pulumiType;
    }

    public /*out*/ readonly randomResult!: pulumi.Output<string>;

    /**
     * Create a Component resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ComponentArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.length === undefined) && !opts.urn) {
                throw new Error("Missing required property 'length'");
            }
            resourceInputs["length"] = args ? args.length : undefined;
            resourceInputs["randomResult"] = undefined /*out*/;
        } else {
            resourceInputs["randomResult"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Component.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a Component resource.
 */
export interface ComponentArgs {
    /**
     * Length of the Component
     */
    length: pulumi.Input<number>;
}
