achrolabutils contains useful scripts for running the vision laboratory.
TODO: add more details

achrolabutils contains module achrolab and two submodules eyeone and wasco.

To get started with github and to become a contributing member to these
repositories do the following:

Open git bash and clone achrolabutils

    git clone git@github.com:derNarr/achrolabutils.git

then run

    cd achrolabutils
    git submodule update --recursive --init

Now you have all repositories on your machine.

When you want to get writing access (you are allowed to and want to), run

    cd achrolab
    git remote rm origin
    git remote add origin git@github.com:derNarr/achrolab.git
    
    cd eyeone
    git remote rm origin
    git remote add origin git@github.com:derNarr/eyeone.git
    
    cd ../wasco
    git remote rm origin
    git remote add origin git@github.com:derNarr/wasco.git

For more relevant documentation see
github.com/derNarr/achrolab/tree/master/doc.

