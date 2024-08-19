package pkg

import (
	"github.com/pulumi/pulumi-go-provider/infer"
	random "github.com/pulumi/pulumi-random/sdk/v4/go/random"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Component struct{}
type ComponentArgs struct {
	Length pulumi.IntInput `pulumi:"length"`
}

func (c *ComponentArgs) Annotate(a infer.Annotator) {
	a.Describe(&c.Length, "Length of the Component")
}

type ComponentState struct {
	pulumi.ResourceState

	RandomResult pulumi.StringOutput `pulumi:"randomResult"`
}

func (c *Component) Construct(ctx *pulumi.Context, name string, typ string, args ComponentArgs, opts pulumi.ResourceOption) (*ComponentState, error) {
	comp := &ComponentState{}
	ctx.RegisterComponentResource(typ, name, comp, opts)
	randomString, err := random.NewRandomString(ctx, name, &random.RandomStringArgs{
		Length: args.Length,
	}, pulumi.Parent(comp))
	if err != nil {
		return nil, err
	}

	comp.RandomResult = randomString.Result
	return comp, nil
}
